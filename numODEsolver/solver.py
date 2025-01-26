import sympy as sp
from scipy.interpolate import interp1d
import numpy as np

class solver:
# get_function() -> Takes a function of x and y as an input. Make sure to use correct python syntax and put everything in curved brackets.
#   --> Example: numODEsolver.get_function("x+y"), The diff.eq. would then be: y' = x+y and it will be numerically solved for y.
    def get_function(self,func):
        x,y = sp.symbols("x y")
        func = sp.sympify(func)
        f = sp.lambdify((x,y), func, "numpy")
        return f

# same get_function method, just for 2nd order odes you. Example: y'' = -y,
    def get_function_2order(self,func):
        x,y,dy = sp.symbols("x y dy")
        func = sp.sympify(func)
        f = sp.lambdify((x,y,dy), func, "numpy")
        return f

# You can choose between 2 methods to solve the ODE numerically : euler and rk4. Those take the function f from before
#  as an input and 2 Initial conditions x0 and y0 as well as an x-axis bound. If n is a high number the result will be more accurate.
# Both return arrays with the x,y values

# solves the ode with initial conditions y(x0) , dy(x0)
    def solve_euler_2order(self,f,x0,y0,dy0,n,bound):
        if n <= 0:
            raise ValueError("n must be greater than zero.")
        y = [y0]
        dy = [dy0]
        x = [x0]
        h = (bound-x0)/n
        for i in range(n):
            x_e2 = x[-1] + h
            y_e2 = y[-1] + h * dy[-1]
            dy_e2 = dy[-1] + h * f(x[-1],y[-1],dy[-1])

            x.append(x_e2)
            y.append(y_e2)
            dy.append(dy_e2)

        return x,y,dy

    def solve_euler(self,f,x0,y0,n,bound):
        if n <= 0:
            raise ValueError("n must be greater than zero.")
        y = [y0]
        x = [x0]
        h = (bound-x0)/n
        for i in range(n):
            y_e = y[-1] + h * f(x[-1], y[-1])
            x_e = x[-1] + h

            x.append(x_e)
            y.append(y_e)

        return x, y

    def solve_rk4(self,f,x0,y0,n,bound):
        if n <= 0:
            raise ValueError("n must be greater than zero.")
        y = [y0]
        x = [x0]
        h = (bound-x0) / n
        for i in range(n):
            k1 = h * f(x[-1], y[-1])
            k2 = h * f(x[-1] + h / 2, y[-1] + k1 / 2)
            k3 = h * f(x[-1] + h / 2, y[-1] + k2 / 2)
            k4 = h * f(x[-1] + h, y[-1] + k3)

            y_r = y[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x_r = x[-1] + h

            x.append(x_r)
            y.append(y_r)

        return x, y

# Allows you to get the y-value from a specific x-value
# You can adjust the decimal places, note that rk4 is more accurate
    def get_value(self,x,y,val,dec):
        function = interp1d(x,y,kind="cubic")
        num = np.round(function(val),dec)
        return num