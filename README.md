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
import matplotlib.pyplot as plt #optional for plot

solver = solver()
f = solver.get_function("y") 
x,y = solver.solve_rk4(f,x0=0,y0=1,n=10000,bound=10.1)
print(solver.get_value(x,y,val=10,dec=5))
```
```bash
from numODEsolver import solver

solver = solver()
f = solver.get_function_2order("dy")
x,y,dy = solver.solve_euler_2order(f,x0=0,y0=1,dy0=1,n=10000,bound=5)
print(solver.get_value(x,y,val=3,dec=2))
```

# Version History

-  8.12.2024 - v0.1 -> only 1st order ODE's are solvable, more features coming soon
- 15.12.2024 - v0.2 -> removed plot function
- 26.1.2025 - v0.3 -> included 2nd order methods, see more on GitHub

---
For more documentation take a look at the source code on my GitHub.

You can modify the script to add more methods, adjust default parameters, or change visualization settings.

This project is open-source and free to use. Contributions and suggestions are welcome!

Lukas

