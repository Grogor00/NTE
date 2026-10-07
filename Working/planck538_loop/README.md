# Planck-comparable recovery loop

**Stop:** `python Working/planck538_loop/orchestrate.py request-stop`  
or create file `Working/planck538_loop/STOP`  
or tell the agent: **stop** / **stop the planck loop**.

**Status:** `python Working/planck538_loop/orchestrate.py status`

**Manual seed / score:**
```
python Working/planck538_loop/orchestrate.py seed-round
python Working/planck538_loop/orchestrate.py score
```

Wake sentinel: `AGENT_LOOP_TICK_planck538` every 10 minutes (local PowerShell loop).

Success = gates **V+C+A+L** (decimal alone is not enough; κ≈5.50 already in V band).
