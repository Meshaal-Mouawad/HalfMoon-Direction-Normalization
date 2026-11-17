#!/usr/bin/env python3
"""Diagnostics for the proved fixed-decoder radius-error corollary.
No model fitting; all points below are constructed geometric diagnostics.
Dependencies: numpy, sympy. Run: python verify_radius_error.py --output radius_error_verification.json
"""
import argparse,hashlib,json,platform
from pathlib import Path
import numpy as np
import sympy as sp

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=Path('radius_error_verification.json'));a=p.parse_args()
 Q=sp.Rational;alpha=sp.sqrt(221)/20;beta=sp.sqrt((29761+440*sp.sqrt(1671))/72400)
 star=(alpha+beta)/2;epsstar=(beta-alpha)/2
 exact={'equal_lower_margin':sp.simplify(star-alpha-epsstar)==0,'equal_upper_margin':sp.simplify(beta-star-epsstar)==0,'experimental_upper_margin_is_smaller':bool(beta-Q(4,5)<Q(4,5)-alpha),'epsilon_positive':bool(epsstar>0)}
 assert all(exact.values())
 lo,hi,ts=float(alpha),float(beta),float(star)
 rr,aa=np.meshgrid(np.linspace(.800001,1.199999,241),np.linspace(.000001,np.pi-.000001,1001),indexing='ij')
 x0=np.c_[rr.ravel()*np.cos(aa.ravel()),rr.ravel()*np.sin(aa.ravel())]
 x=np.r_[x0,np.array([1.,.5])-x0];y=np.r_[np.zeros(len(x0),dtype=int),np.ones(len(x0),dtype=int)]
 v=x-[.5,.25];r=np.linalg.norm(v,axis=1)
 near=(9*v[:,0]+10*v[:,1]<=0).astype(int);far=(v[:,1]-v[:,0]<=0).astype(int)
 grid=[]
 for t in [lo,.75,ts,.78,.8,.81,hi]:
  margin=min(t-lo,hi-t)
  # Test every attainable bin at each point, not just a few sampled errors.
  near_possible=r-margin<=t;far_possible=r+margin>t
  worst=(near_possible&(near!=y))|(far_possible&(far!=y))
  errors=int(np.count_nonzero(worst));assert errors==0
  grid.append({'threshold':t,'epsilon':margin,'points':len(x),'points_with_any_admissible_error_causing_wrong_decision':errors})
 theta=float(sp.atan2((350+9*sp.sqrt(1671))/905,(63-2*sp.sqrt(1671))/181));witnesses=[]
 for t in [.75,ts,.8,.81]:
  for side in ['lower','upper']:
   eps=(t-lo if side=='lower' else hi-t)+1e-4
   error=eps if side=='lower' else -eps
   s,angle=(1.2-1e-7,1e-7) if side=='lower' else (.8+1e-7,theta+1e-6)
   xx=np.array([s*np.cos(angle),s*np.sin(angle)]);vv=xx-[.5,.25];radius=float(np.linalg.norm(vv));measured=radius+error
   score=float(9*vv[0]+10*vv[1] if measured<=t else vv[1]-vv[0])
   assert .8<float(np.linalg.norm(xx))<1.2 and xx[1]>0 and score<0
   witnesses.append({'threshold':t,'failed_margin':side,'epsilon':eps,'constant_error':error,'class0_interior_point':xx.tolist(),'radius':radius,'measured_radius':measured,'selected_score':score,'wrong_class':1})
 result={'scope':'V9 constructed geometric diagnostics; exact direction, h=0.5, fixed midpoint and angular rules','exact_checks':exact,'alpha':str(sp.N(alpha,40)),'beta':str(sp.N(beta,40)),'optimal_threshold':str(sp.N(star,40)),'maximum_tolerance':str(sp.N(epsstar,40)),'tolerance_at_0.8':str(sp.N(beta-Q(4,5),40)),'constructed_grid':grid,'strict_outside_witnesses':witnesses,'fresh_neural_fits':0,'saved_observation_replay_performed':False,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'environment':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__}}
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'symbolic':exact,'constructed_points':len(x),'thresholds':len(grid),'all_worst_bin_errors':0,'strict_counterexamples':len(witnesses),'t_star':result['optimal_threshold'],'epsilon_star':result['maximum_tolerance']},indent=2))
if __name__=='__main__':main()
