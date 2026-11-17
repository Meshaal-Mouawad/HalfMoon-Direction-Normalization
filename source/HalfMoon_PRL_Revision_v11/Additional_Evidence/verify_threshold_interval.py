#!/usr/bin/env python3
"""Check the analytic threshold interval for the fixed Half-Moon decoder.

No model is trained and no original study file is changed. The symbolic checks
and diagnostic points complement the proof in Threshold_Addendum.tex. Optional
replay uses the ten pre-existing test arrays in the V3 reproducibility archive.
Usage: python verify_threshold_interval.py --archive PATH --output result.json
Dependencies: Python 3, numpy, sympy.
"""
from __future__ import annotations
import argparse, hashlib, io, json, platform, zipfile
from pathlib import Path
import numpy as np
import sympy as sp


def decode(x: np.ndarray, threshold: float) -> np.ndarray:
    v = np.asarray(x, dtype=float) - np.array([0.5, 0.25])
    r = np.linalg.norm(v, axis=1)
    s = np.where(r <= threshold, 9*v[:,0]+10*v[:,1], v[:,1]-v[:,0])
    return (s <= 0).astype(np.uint8)  # matches the theorem's 'class 0 iff >0'


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive', type=Path)
    p.add_argument('--output', type=Path, default=Path('threshold_verification.json'))
    a=p.parse_args()
    Q=sp.Rational
    lower=sp.sqrt(221)/20
    upper=sp.sqrt((29761+440*sp.sqrt(1671))/72400)
    xs=(63-2*sp.sqrt(1671))/181
    ys=(350+9*sp.sqrt(1671))/905
    checks={
        'inner_circle_intersection': sp.simplify(xs**2+ys**2-Q(16,25)) == 0,
        'near_boundary_line': sp.simplify(9*xs+10*ys-7) == 0,
        'upper_endpoint_radius': sp.simplify((xs-Q(1,2))**2+(ys-Q(1,4))**2-upper**2) == 0,
        'lower_endpoint_radius': sp.simplify((Q(6,5)-Q(1,2))**2+Q(1,4)**2-lower**2) == 0,
        'radial_derivative_positive': bool(Q(8,5) > sp.sqrt(5)/2),
        'inner_intersection_upper_halfplane': bool(ys>0),
        'inner_intersection_second_quadrant': bool(xs<0),
        'safe_inner_interval': bool(lower<Q(3,4)) and bool(Q(81,100)<upper),
        'strict_endpoint_order': bool(lower<upper),
        'noncircular_vertex_below_lower_bound': bool(Q(1,8)<lower**2),
    }
    assert all(checks.values()), checks
    lo, hi=float(lower),float(upper)
    ts=[lo,.75,.78,.8,.81,hi]
    # Interior geometric diagnostic: not a sample of observed data or a proof.
    radii=np.linspace(.800001,1.199999,241)
    angles=np.linspace(.000001,np.pi-.000001,1001)
    rr,aa=np.meshgrid(radii,angles,indexing='ij')
    x0=np.column_stack((rr.ravel()*np.cos(aa.ravel()),rr.ravel()*np.sin(aa.ravel())))
    x1=np.array([1.,.5])-x0
    x=np.vstack((x0,x1)); y=np.r_[np.zeros(len(x0),np.uint8),np.ones(len(x1),np.uint8)]
    grid=[{'threshold':t,'errors':int(np.count_nonzero(decode(x,t)!=y)), 'n':len(y)} for t in ts]
    assert all(r['errors']==0 for r in grid)
    # Sharpness witnesses have strict support and wrong-class inequalities;
    # continuity supplies open neighborhoods of errors, as in the proof.
    theta=float(sp.atan2(ys,xs)); witnesses=[]
    for side,t in [('below',lo-1e-4),('above',hi+1e-4)]:
        eps=1e-7
        s,angle=(1.2-eps,eps) if side=='below' else (.8+eps,theta+10*eps)
        point=np.array([[s*np.cos(angle),s*np.sin(angle)]])
        v=point[0]-[.5,.25]; radius=float(np.linalg.norm(v))
        score=float(9*v[0]+10*v[1]) if radius<=t else float(v[1]-v[0])
        assert .8<float(np.linalg.norm(point))<1.2 and point[0,1]>0
        assert score<0 and int(decode(point,t)[0])==1
        witnesses.append({'side':side,'threshold':t,'class0_point':point[0].tolist(),
                          'distance_from_origin':float(np.linalg.norm(point)),
                          'distance_from_midpoint':radius,'selected_score':score,'predicted_class':1})
    replay=[]; archive_sha=None
    if a.archive:
        archive_sha=hashlib.sha256(a.archive.read_bytes()).hexdigest()
        with zipfile.ZipFile(a.archive) as z:
            prefix='HalfMoon_PRL_Reproducibility_v3/research/extensions/radial_bit_v3/confirmatory/test_observations/'
            files=sorted(n for n in z.namelist() if n.startswith(prefix) and n.endswith('.npz'))
            assert len(files)==10, f'Expected ten existing test arrays, got {len(files)}'
            for n in files:
                raw=z.read(n)
                with np.load(io.BytesIO(raw),allow_pickle=False) as d:
                    xx=d['x']; yy=(d['y']>0).astype(np.uint8)
                    er=[int(np.count_nonzero(decode(xx,t)!=yy)) for t in ts]
                    assert all(e==0 for e in er)
                    replay.append({'member':n,'sha256':hashlib.sha256(raw).hexdigest(),
                                   'n':len(yy),'errors_in_threshold_order':er})
    result={'scope':'V8 analytic extension; fixed decoder, h=0.5, midpoint=(0.5,0.25)',
            'lower_exact':str(lower),'upper_exact':str(upper),'lower':lo,'upper':hi,
            'endpoint_decimal_digits_30':[str(sp.N(lower,30)),str(sp.N(upper,30))],
            'safe_inner_interval':[.75,.81], 'symbolic_checks':checks,
            'thresholds':ts,'constructed_interior_grid':grid,'sharpness_witnesses':witnesses,
            'existing_test_replay':replay,'existing_observations_total':sum(r['n'] for r in replay),
            'source_archive_sha256':archive_sha,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'environment':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},
            'interpretation':'The analytic proof establishes every support point and all real thresholds in the interval. Grid/replay are diagnostics. Outside this interval the stated decoder fails; optimality across alternative decoders is not asserted. No new neural training or independent test sample was performed.'}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'endpoints':[lo,hi],'symbolic_checks':checks,'grid_points':len(y),
                      'replayed_observations':result['existing_observations_total'],
                      'all_in_interval_errors':0,'outside_witnesses':witnesses},indent=2))
if __name__=='__main__': main()
