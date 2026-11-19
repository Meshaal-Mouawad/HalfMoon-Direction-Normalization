#!/usr/bin/env python3
"""Independent deterministic checks for HM-IV-2026-01; Python standard library only."""
from __future__ import annotations

import argparse
import ast
import hashlib
import io
import json
import math
import platform
import struct
import sys
import zipfile
from array import array
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction as Q
from pathlib import Path
from math import isqrt

A, B = 0.8, 1.2
H = math.pi * (B * B - A * A) / 2
SCALE = 10**48


class I:
    """Closed rational enclosure; operations retain outward bounds exactly."""

    def __init__(self, lo, hi=None):
        self.lo = Q(lo)
        self.hi = Q(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def cv(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        other = self.cv(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -self.cv(other)

    def __rsub__(self, other):
        return self.cv(other) - self

    def __mul__(self, other):
        other = self.cv(other)
        z = (self.lo * other.lo, self.lo * other.hi,
             self.hi * other.lo, self.hi * other.hi)
        return I(min(z), max(z))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.cv(other)
        assert other.lo > 0 or other.hi < 0
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return self.cv(other) / self

    def sqrt(self):
        assert self.lo >= 0
        def floor_root(q):
            return isqrt((q.numerator * SCALE * SCALE) // q.denominator)
        return I(Q(floor_root(self.lo), SCALE),
                 Q(floor_root(self.hi) + 1, SCALE))

    def out(self, digits=28):
        with localcontext() as ctx:
            ctx.prec = digits + 12
            ctx.rounding = ROUND_FLOOR
            lo = Decimal(self.lo.numerator) / Decimal(self.lo.denominator)
            ctx.rounding = ROUND_CEILING
            hi = Decimal(self.hi.numerator) / Decimal(self.hi.denominator)
            return [str(lo), str(hi)]


def atan_bounds(q, n):
    q = Q(q)
    terms = [(-1)**k / ((2*k + 1) * q**(2*k + 1)) for k in range(n)]
    partial = sum(terms, Q(0))
    next_term = (-1)**n / ((2*n + 1) * q**(2*n + 1))
    return I(min(partial, partial + next_term),
             max(partial, partial + next_term))


PI = 16 * atan_bounds(5, 75) - 4 * atan_bounds(239, 20)


def certificate(h):
    if h == Q(1, 2):
        rho, delta = I(Q(1, 8)), I(Q(1, 8))
        m = I(Q(43, 40)) + I(5).sqrt() / 4
    else:
        assert h == 1
        rho, delta = I(Q(1, 20)), I(Q(1, 8))
        m = I(Q(11, 10)) + I(2).sqrt() / 2
    c = (I(3).sqrt() * rho * rho +
         (3 * rho * rho * rho * rho + 256 * delta * delta * m * m).sqrt()) / (16 * delta)
    compact = I(3).sqrt() * rho * rho * rho / (2 * (c + m))
    exterior = 4 * rho * delta * (1 - m / c)
    shape = I(min(compact.lo, exterior.lo), min(compact.hi, exterior.hi))
    return {"rho": rho.out(), "delta": delta.out(), "M": m.out(),
            "C_star": c.out(), "compact_factor": compact.out(),
            "exterior_factor": exterior.out(),
            "area_probability": (I(5) / (4 * PI) * shape).out(),
            "radius_probability": (I(25) / (24 * PI) * shape).out()}


def support(x, y, label, h):
    if label == 0:
        return A*A < x*x + y*y < B*B and y > 0
    return A*A < (x-1)**2 + (y-h)**2 < B*B and y < h


def decoder(x, y, threshold, error=0.0):
    vx, vy = x-0.5, y-0.25
    radius = math.hypot(vx, vy)
    assert radius > 0
    far = radius + error > threshold
    return 0 if ((vy-vx > 0) if far else (9*vx+10*vy > 0)) else 1


def midpoint_grid(thresholds):
    counts = {str(t): 0 for t in thresholds}
    n = 0
    # Open support midpoint grid; both labels are checked independently.
    for j in range(96):
        radius = A + (B-A)*(j+0.5)/96
        for k in range(720):
            angle = math.pi*(k+0.5)/720
            x, y = radius*math.cos(angle), radius*math.sin(angle)
            assert support(x, y, 0, 0.5)
            for label, px, py in ((0, x, y), (1, 1-x, 0.5-y)):
                assert support(px, py, label, 0.5)
                n += 1
                for t in thresholds:
                    counts[str(t)] += decoder(px, py, t) != label
    return n, counts


def ray_events(c, u, h):
    cx, cy = c
    ux, uy = u
    max_r = max(math.hypot(cx, cy), math.hypot(cx-1, cy-h)) + B + 1
    events = [0.0, max_r]
    for mx, my in ((0, 0), (1, h)):
        dx, dy = cx-mx, cy-my
        dot = dx*ux + dy*uy
        for radius in (A, B):
            disc = dot*dot - (dx*dx + dy*dy-radius*radius)
            if disc >= 0:
                root = math.sqrt(disc)
                events.extend(v for v in (-dot-root, -dot+root) if 0 < v < max_r)
    if abs(uy) > 1e-15:
        events.extend(v for v in ((-cy)/uy, (h-cy)/uy) if 0 < v < max_r)
    return sorted(events)


def ray_cancellation(c, angle, h):
    u = (math.cos(angle), math.sin(angle))
    edges = ray_events(c, u, h)
    pos = neg = 0.0
    for lo, hi in zip(edges, edges[1:]):
        if hi-lo < 1e-12:
            continue
        r = (lo+hi)/2
        x, y = c[0]+r*u[0], c[1]+r*u[1]
        in0, in1 = support(x,y,0,h), support(x,y,1,h)
        mass = (hi*hi-lo*lo)/(4*H)  # 0.5 prior / H density times polar integral
        if in0 and not in1:
            pos += mass
        elif in1 and not in0:
            neg += mass
    return min(pos, neg)


def area_loss(c, h, n=4096):
    p = (0.5, h/2)
    distance = math.dist(c, p)
    bound = B + math.hypot(*p)
    if distance > bound:
        theta0 = math.atan2(p[1]-c[1], p[0]-c[0])
        halfwidth = math.asin(min(1.0, bound/distance))
        start, width = theta0-halfwidth, 2*halfwidth
    else:
        start, width = 0.0, 2*math.pi
    return width * sum(ray_cancellation(c, start+width*(j+0.5)/n, h)
                       for j in range(n)) / n


def overlap_area(h=1.0, n=200000):
    def x_intervals(y, mx, my):
        dy = y-my
        if abs(dy) >= B:
            return []
        outer = math.sqrt(B*B-dy*dy)
        inner = math.sqrt(max(0.0, A*A-dy*dy))
        return [(mx-outer, mx-inner), (mx+inner, mx+outer)] if abs(dy) < A else [(mx-outer,mx+outer)]
    total = 0.0
    for j in range(n):
        y = h*(j+0.5)/n
        p0, p1 = x_intervals(y,0,0), x_intervals(y,1,h)
        total += sum(max(0.0,min(v,z)-max(u,w))
                     for u,v in p0 for w,z in p1)
    return h*total/n


def npy_from_npz(outer, path, key):
    with zipfile.ZipFile(io.BytesIO(outer.read(path))) as inner:
        data = inner.read(key+'.npy')
    assert data[:6] == b'\x93NUMPY'
    major = data[6]
    if major == 1:
        length = struct.unpack_from('<H',data,8)[0]
        offset = 10
    else:
        length = struct.unpack_from('<I',data,8)[0]
        offset = 12
    header = ast.literal_eval(data[offset:offset+length].decode('latin1'))
    assert not header['fortran_order']
    raw = data[offset+length:]
    if header['descr'] == '<f8':
        assert sys.byteorder == 'little'
        values = array('d')
        values.frombytes(raw)
    elif header['descr'] == '|u1':
        values = raw
    else:
        raise ValueError('unsupported NPY dtype '+header['descr'])
    assert len(values) == math.prod(header['shape'])
    return values, header['shape']


def replay_frozen(outer, thresholds):
    root = 'HalfMoon_PRL_Research_Data_v11/research/extensions/radial_bit_v3/confirmatory/'
    counts = {'R':0,'DM':0,'B':0,'PM':0,'explicit':0}
    errors = {str(t):0 for t in thresholds}
    seed_rows = []
    total = 0
    outside = 0
    for seed in range(2001,2011):
        obs = root+f'test_observations/g0_s{seed}_test.npz'
        coords, shape = npy_from_npz(outer,obs,'x')
        labels, label_shape = npy_from_npz(outer,obs,'y')
        assert shape == (50000,2) and label_shape == (50000,)
        preds = {}
        for rep in ('R','DM','B','PM'):
            path = root+f'test_predictions/radialbit_g0_s{seed}_{rep}_h64_a1.npz'
            preds[rep], pred_shape = npy_from_npz(outer,path,'predicted_class')
            assert pred_shape == (50000,)
        explicit, pred_shape = npy_from_npz(
            outer,root+f'test_predictions/explicit_decoder_s{seed}.npz','predicted_class')
        assert pred_shape == (50000,)
        row = {'seed':seed,'n':50000,'errors':{k:0 for k in counts}}
        for i in range(50000):
            x, y = coords[2*i], coords[2*i+1]
            assert labels[i] in (-1.0,1.0)
            label = 0 if labels[i] == -1.0 else 1
            outside += not support(x,y,label,.5)
            for t in thresholds:
                errors[str(t)] += decoder(x,y,t) != label
            for rep in counts:
                predicted = explicit[i] if rep == 'explicit' else preds[rep][i]
                row['errors'][rep] += predicted != label
        for rep in counts:
            counts[rep] += row['errors'][rep]
        total += 50000
        seed_rows.append(row)
    summary = json.loads(outer.read(root+'analysis_summary.json'))
    expected = {r['representation']:r['total_errors'] for r in summary['summaries']}
    return {'observations':total,'outside_declared_support':outside,
            'decoder_errors_by_threshold':errors,'prediction_errors':counts,
            'published_summary_errors':expected,'seed_rows':seed_rows,
            'counts_match_summary':all(counts[k]==expected[k] for k in expected)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-dir', type=Path, help='temporary authoritative source download')
    ap.add_argument('--research-archive', type=Path, help='original frozen research release zip')
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    alpha = I(221).sqrt()/20
    beta = ((I(29761)+440*I(1671).sqrt())/72400).sqrt()
    a, b = map(float, (alpha.out()[0], beta.out()[0]))
    tstar = (a+b)/2
    checks = []
    def check(name, passed, detail):
        checks.append({"name":name,"passed":bool(passed),"detail":detail})
    certs = {"0.5": certificate(Q(1,2)), "1": certificate(Q(1))}
    claimed = {"0.5": (Q('0.0002050842462841'),Q('0.0001709035385701')),
               "1": (Q('0.0000119104106520'),Q('0.0000099253422100'))}
    for h, values in certs.items():
        for law, stated in zip(('area_probability','radius_probability'),claimed[h]):
            lower = Q(values[law][0])
            check('certificate_'+h+'_'+law, lower >= stated,
                  {"certified_lower":values[law][0],"published_downward":str(stated)})
    check('threshold_order', a < 0.8 < b, {"alpha":alpha.out(),"beta":beta.out()})
    xstar = (63-2*math.sqrt(1671))/181
    ystar = (350+9*math.sqrt(1671))/905
    check('beta_boundary_identity', abs(math.hypot(xstar-.5,ystar-.25)-b)<1e-13 and
          abs(xstar*xstar+ystar*ystar-A*A)<1e-13 and abs(9*xstar+10*ystar-7)<1e-13,
          {"x_star":xstar,"y_star":ystar})
    check('support_collision', support(1,.25,0,.5) and support(2,.25,1,.5) and
          support(.9,.1,0,1) and support(.9,.1,1,1), {})
    check('transition_and_open_boundaries',
          support(.81,.0001,0,.78) and support(.81,.0001,1,.78) and
          not support(1.2,0,0,.5) and not support(xstar,ystar,0,.5),
          {"above_transition_overlap_point":[.81,.0001],"h":.78,
           "excluded_extremizers":[[1.2,0],[xstar,ystar]]})
    thresholds = [a,0.75,tstar,0.8,0.81,b]
    points, grid_errors = midpoint_grid(thresholds)
    check('open_support_decoder_grid', all(v==0 for v in grid_errors.values()),grid_errors)
    boundary = {}
    for side, t in [('below_alpha',a-1e-4),('above_beta',b+1e-4)]:
        if side=='below_alpha':
            x,y = B-1e-7,1e-7
        else:
            theta = math.atan2(ystar,xstar)+1e-5
            x,y = (A+1e-9)*math.cos(theta),(A+1e-9)*math.sin(theta)
        boundary[side] = {"point":[x,y],"threshold":t,
                          "in_S0":support(x,y,0,.5),"decoded":decoder(x,y,t),
                          "radius":math.hypot(x-.5,y-.25)}
        check('sharp_'+side,boundary[side]['in_S0'] and boundary[side]['decoded']==1,boundary[side])
    tol08 = b-.8
    tolstar = (b-a)/2
    check('radius_tolerance_identities',tol08>0 and tolstar>tol08,
          {"at_0.8":tol08,"at_optimum":tolstar,"optimum_threshold":tstar})
    # Constant errors outside each margin realize the geometric counterexamples.
    below = boundary['below_alpha']['point']
    above = boundary['above_beta']['point']
    check('radius_error_counterexamples',
          decoder(*below,.8,error=.8-(a-1e-4))==1 and
          decoder(*above,.8,error=.8-(b+1e-4))==1,{})
    origins = [(0,0),(0.5,.25),(0,3),(1,.25),(2,.25),(.8,0),
               (.5,10.25),(.5,100.25),(.5,1000.25)]
    losses = {str(c):area_loss(c,.5,8192) for c in origins}
    checks.append({"name":"finite_origin_exploration_positive","passed":all(v>0 for v in losses.values()),
                   "detail":"finite deterministic search only"})
    frozen_area = {'(0, 0)':.11857683,'(0.5, 0.25)':.10747927,'(0, 3)':.21150860}
    check('published_area_floors_h05',all(abs(losses[k]-v)<.0001 for k,v in frozen_area.items()),
          {"reference":frozen_area,"absolute_probability_tolerance":.0001})
    raw_overlap = overlap_area()
    raw_risk = raw_overlap/(2*H)
    check('published_area_raw_risk_h1',abs(raw_risk-.06715750)<.0001,
          {"recalculated":raw_risk,"published":.06715750,"tolerance":.0001})
    h1_origins = [(0,0),(.5,.5),(0,3),(1,.25),(.8,0),(.5,10.5),(.5,100.5)]
    h1_losses = {str(c):area_loss(c,1.0,8192) for c in h1_origins}
    check('finite_origin_exploration_positive_h1',all(v>0 for v in h1_losses.values()),
          'finite deterministic search only')
    h1_frozen = {'(0, 0)':.21729441,'(0.5, 0.5)':.20854811,'(0, 3)':.20598715}
    check('published_area_floors_h1',
          all(abs(raw_risk+h1_losses[k]-v)<.0001 for k,v in h1_frozen.items()),
          {"reference_direction_risks":h1_frozen,"absolute_probability_tolerance":.0001})
    control_losses = {str(c):area_loss(c,-.25,8192) for c in ((0,0),(.5,-.125))}
    check('negative_displacement_control',all(abs(v)<1e-12 for v in control_losses.values()),
          control_losses)
    source = {}
    if args.source_dir:
        for name in ('Full_Manuscript.tex','Full_Theory.tex','Full_Manuscript.pdf','Full_Article_Source.zip'):
            p = args.source_dir/name
            source[name] = {"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"bytes":p.stat().st_size} if p.exists() else None
        check('authoritative_source_available',all(source.values()),source)
    archive = {'status':'not_provided'}
    frozen = {'status':'not_provided'}
    if args.research_archive:
        if args.research_archive.exists():
            with zipfile.ZipFile(args.research_archive) as z:
                names=z.namelist()
                bad=z.testzip()
                if bad is None:
                    frozen = replay_frozen(z,thresholds)
                    check('frozen_observation_supports',frozen['outside_declared_support']==0,
                          {'observations':frozen['observations'],'outside':frozen['outside_declared_support']})
                    check('frozen_decoder_replay',all(v==0 for v in frozen['decoder_errors_by_threshold'].values())
                          and frozen['prediction_errors']['explicit']==0,
                          frozen['decoder_errors_by_threshold'])
                    check('frozen_prediction_count_replay',frozen['counts_match_summary'],frozen['prediction_errors'])
            digest=hashlib.sha256()
            with args.research_archive.open('rb') as stream:
                for block in iter(lambda:stream.read(1024*1024),b''):
                    digest.update(block)
            archive={"status":"zip_integrity_pass" if bad is None else "zip_integrity_fail",
                     "sha256":digest.hexdigest(),
                     "entries":len(names),"bad_entry":bad,
                     "matching_evidence_names":[x for x in names if any(w in x.lower() for w in ('threshold','certificate','results'))][:80]}
            check('research_archive_integrity',bad is None,archive['status'])
        else:
            archive={'status':'missing_path','path':str(args.research_archive)}
            check('research_archive_integrity',False,archive)
    result={"review_id":"HM-IV-2026-01","reviewer":"Elias Veyron",
            "authoritative_remote_main":"42e857497e4d6988f8e1178a9b91a7e45902dcc6",
            "execution_outcome":"PASS" if all(x['passed'] for x in checks) else "FAILED_CHECKS",
            "python":sys.version,"platform":platform.platform(),"random_seed":None,
            "deterministic":True,"comparison_tolerances":{"boundary_identity":1e-13,
            "published_floor_probability":.0001,"rational_sqrt_grid_decimal_places":48,
            "display_interval_significant_digits":40},
            "pi_interval":PI.out(),"thresholds":{"alpha":alpha.out(),"beta":beta.out(),
            "t_star":tstar,"epsilon_star":tolstar,"epsilon_at_0.8":tol08},
            "certificates":certs,"grid":{"support_points":points,"decoder_evaluations":points*len(thresholds),
            "errors":grid_errors},"boundary":boundary,"origin_area_losses_h05":losses,
            "h1_area_raw_risk":raw_risk,"origin_area_losses_h1":h1_losses,
            "negative_h_control_losses":control_losses,"sources":source,"archive":archive,
            "frozen_evidence_replay":frozen,
            "checks":checks,"check_count":len(checks),
            "failed_checks":[x for x in checks if not x['passed']]}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({"execution_outcome":result['execution_outcome'],
                      "check_count":len(checks),"failed_checks":result['failed_checks']}))
    return 0 if all(x['passed'] for x in checks) else 1


if __name__=='__main__':
    raise SystemExit(main())
