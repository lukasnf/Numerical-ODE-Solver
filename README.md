# Numerical ODE Solver

This project is a Python implementation for solving ordinary differential equations (ODEs) numerically. The script allows users to choose between two methods: Euler's Method and Runge-Kutta 4th Order Method (RK4), providing a visual representation of the solution.

## Requirements
Python version >= 3.8

Ensure the following Python libraries are installed:

Install it using `pip`:
```bash
pip install numODEsolver
```
## Example
```bash
from numODEsolver import solver
import numpy as np #optional for constants 

solver = solver()
f = solver.get_function("cos(x)") , f = solver.get_function("diff(y)")
x,y = solver.solve_rk4(f,x0=0,y0=1,n=10000,bound=10.1)
solver.plot(x,y,xlabel="x",ylabel="y",title="rk4")
print(solver.get_value(x,y,val=10,dec=5)
```

# Version History

-  8.12.2024 - v0.1 -> only 1st order ODE's are solvable, more features coming soon


---
For more documentation take a look at the source code on my GitHub.

You can modify the script to add more methods, adjust default parameters, or change visualization settings.

This project is open-source and free to use. Contributions and suggestions are welcome!

Lukas

