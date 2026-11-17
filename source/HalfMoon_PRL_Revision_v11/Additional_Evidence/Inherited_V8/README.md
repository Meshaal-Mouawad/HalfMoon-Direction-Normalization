# Threshold interval evidence

This package accompanies Proposition 1 in Threshold_Addendum.pdf. It establishes the operating interval of the fixed near/far angular decoder at h=0.5 and c=(0.5,0.25).

Run symbolic, constructed-grid and counterexample checks:

```bash
python verify_threshold_interval.py --output threshold_verification.json
```

Replay the same ten pre-existing test arrays as well:

```bash
python verify_threshold_interval.py --archive /path/to/HalfMoon_PRL_Reproducibility_v3.zip --output threshold_verification.json
```

Dependencies: Python 3, numpy and sympy. The script writes only the requested JSON output; it never changes the input archive, trains a network, or alters frozen predictions. The provided output includes the actual tested library versions, archive SHA-256 and input-member hashes. Observations replayed at six thresholds are the same 500,000 observations, not 3,000,000 independent observations.

The analytic proof is authoritative for the continuum of thresholds/support points. The grid and replay are implementation diagnostics. The maximal interval refers to the stated fixed decoder; no optimality over other decoders or other centers is asserted.
