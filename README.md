# numODEsolver


![PyPI](https://img.shields.io/pypi/v/numODEsolver)
![Python](https://img.shields.io/pypi/pyversions/numODEsolver)

A lightweight Python package for solving first- and second-order ordinary differential equations (ODEs) numerically, using Euler-type methods or the classical fourth-order Runge–Kutta method (RK4).

## Methods

| Solver | ODE | Method | Global error |
| :--- | :--- | :--- | :--- |
| `euler_1order` | y' = f(x, y) | Explicit Euler | ∝ h |
| `rk4_1order` | y' = f(x, y) | Classical RK4 | ∝ h⁴ |
| `euler_2order` | y'' = f(x, y, y') | Semi-implicit Euler (Euler–Cromer) | ∝ h |
| `rk4_2order` | y'' = f(x, y, y') | Classical RK4 | ∝ h⁴ |

Halving the step size *h* reduces the error roughly by a factor of 2 for Euler and by a factor of 16 for RK4.

![Error convergence of Euler and RK4](https://raw.githubusercontent.com/lukasnf/Numerical-ODE-Solver/main/docs/convergence.png)

`euler_2order` updates y' first and then uses the *new* y' to update y. This keeps the energy of oscillating systems (e.g. y'' = −y) bounded, while the plain explicit Euler method lets it grow without limit.

The second-order solvers rewrite y'' = f(x, y, y') as a system of two first-order ODEs, y' = v and v' = f(x, y, v), and advance y and v together.

## Installation

```bash
pip install numODEsolver
```

Requires Python 3.8 or newer. The dependencies [NumPy](https://numpy.org), [SciPy](https://scipy.org) and [asteval](https://github.com/lmfit/asteval) are installed automatically.

## Usage

### First-order ODE

Solve y' = y with y(0) = 1 (exact solution: y = eˣ):

```python
import numODEsolver as ns
import matplotlib.pyplot as plt  # optional, only for plotting

solver = ns.Solver()
f = solver.get_function("y")  # right-hand side of y' = y
values = solver.rk4_1order(f, x0=0, y0=1, n=10000, bound=10)

print(solver.get_value(values, val=10, dec=5))  # y(10) ≈ e^10 = 22026.46579

plt.plot(values[:, 0], values[:, 1])
plt.show()
```

### Second-order ODE

Solve y'' = y' + y with y(0) = 1 and y'(0) = 1:

```python
import numODEsolver as ns

solver = ns.Solver()
f = solver.get_function("y'+y")  # right-hand side of y'' = y' + y; use y' for the first derivative
values = solver.rk4_2order(f, x0=0, y0=1, dy0=1, n=10000, bound=5)

print(solver.get_value(values, val=3, dec=2))  # y(3) ≈ 92.86
```

`euler_2order` takes the same arguments.

### Parameters

| Parameter | Meaning |
| :--- | :--- |
| `x0`, `y0` | Initial point and initial value |
| `dy0` | Initial value of y' (second-order solvers only) |
| `n` | Number of steps (step size h = (bound − x0) / n) |
| `bound` | End of the integration interval, must be greater than `x0` |
| `val`, `dec` | x-value to evaluate and number of decimal places (`get_value`) |

### Return value

Every solver returns a NumPy array with one row per step:

- first-order solvers: columns `[x, y]`
- second-order solvers: columns `[x, y, y']`

`get_value` interpolates y between the steps with a cubic spline. `val` must lie between `x0` and `bound`.

## How Functions Are Parsed

`get_function` turns a string such as `"y'+y"` into a callable function:

1. The string is converted to lower case and every `y'` is replaced by a variable `dy`.
2. The expression is evaluated with [asteval](https://github.com/lmfit/asteval) as `lambda x, y, dy=0: <expression>`.
3. If the expression contains `y'`, the function is marked as second-order.

Allowed are the variables `x`, `y` and `y'`, normal Python operators (`+ - * / **`) and the NumPy math functions and constants without a prefix, e.g. `sin`, `cos`, `exp`, `log`, `sqrt`, `abs`, `pi`:

```python
solver.get_function("sin(x) - y**2")
solver.get_function("-0.5*y' - 4*y")
```

asteval does not allow imports or access to Python internals (like `__import__`), and numODEsolver also removes asteval's `open()`, so expressions cannot read files. This makes it much safer than Python's `eval`, but it is not a complete sandbox, so do not pass untrusted input.

An expression that cannot be parsed raises a `ValueError`. Passing a function with `y'` to a first-order solver also raises a `ValueError`.

## Known Limitations

- Fixed step size only (no adaptive step-size control)
- Explicit methods: stiff ODEs may require very small step sizes
- Integration only forwards (`bound` must be greater than `x0`)
- Only single equations, no systems of several ODEs and no third or higher order
- `get_value` needs at least 4 points (`n >= 3`) for the cubic interpolation
- Functions are evaluated through asteval, which is slower than plain Python; very large `n` can take a while
## Contributing

Bug reports and suggestions are welcome. Please open an [issue](https://github.com/lukasnf/Numerical-ODE-Solver/issues).

## Author

Lukas Filipon, B.Sc. Physics student at KIT
