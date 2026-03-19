# Numerical ODE Solver

This project is a Python implementation for solving ordinary differential equations (ODEs) numerically. The script allows users to choose between two methods: Euler's Method and Runge-Kutta 4th Order Method (RK4), providing a visual representation of the solution (optional). Note: Euler's Method is more inaccurate than RK4.

## Requirements
Python version >= 3.8

Ensure the following Python libraries are installed:

Install it using `pip`:
```bash
pip install numODEsolver
```
## Example
```bash
import numODEsolver as ns
import matplotlib.pyplot as plt #optional for plot

solver = ns.Solver()
f = solver.get_function("y") 
values = solver.rk4_1order(f,x0=0,y0=1,n=10000,bound=10.1)
n = solver.get_value(values,val=10,dec=5)
print(n)
plt.plot(values[:,0],values[:,1])
plt.show()
```
```bash
import numODEsolver as ns

solver = ns.Solver()
f = solver.get_function("y'+y") #y' = for 1st derivative. The ode would be y'' = y'+y
values = solver.euler_2order(f,x0=0,y0=1,dy0=1,n=10000,bound=5)
n = solver.get_value(values,val=3,dec=2)
print(n)
```

# Version History

-  8.12.2024 - v0.1 -> only 1st order ODE's are solvable, more features coming soon
- 15.12.2024 - v0.2 -> removed plot function
- 26.1.2025 - v0.3 -> included 2nd order methods, see more on GitHub
- 19.03.2026 - v2.0 -> more secure function handeling, more stable numerical methods.

---
For more documentation take a look at the source code on my GitHub.

You can modify the script to add more methods, or change visualization settings.

Contributions and suggestions are welcome!

Lukas

