from scipy.interpolate import interp1d
import numpy as np
from asteval import Interpreter


# get_function() -> Takes a function of x and y as an input. Make sure to use correct python syntax and put everything in curved brackets.
#   --> Example: numODEsolver.get_function("x+y"), The diff.eq. would then be: y' = x+y and it will be numerically solved for y.
def get_function(func):
    func = func.lower()
    aeval = Interpreter()
    if not "y'" in func:
        f = aeval(f"lambda x,y: {func}")
        return f
    else:
         func = func.replace("y'","dy")
         f = aeval(f"lambda x,y,dy: {func}")
         return f

def euler_2order(f,x0,y0,dy0,n,bound):
        if n <= 0:
            raise ValueError("n must be greater than zero.")
        elif x0 > bound:
             raise ValueError("initial condition must be < than the input bound!")
        vals = np.zeros((n+1,3))
        vals[0] = [x0,y0,dy0]
        h = (bound-x0)/n
        for i in range(n):
             x,y,dy = vals[i]

             dy_d = dy + h*f(x,y,dy)
             y_d = y + h * dy_d
             x_d = x + h
             vals[i+1] = [x_d,y_d,dy_d]

        return vals

def euler_1order(f,x0,y0,n,bound):
        if n <= 0:
            raise ValueError("n must be greater than zero.")
        elif x0 > bound:
             raise ValueError("initial condition must be < than the inpunt bound!")
        coords = np.zeros((n+1, 2))
        coords[0] = [x0,y0]
        h = (bound-x0)/n
        for i in range(n):
             x,y = coords[i]
             x_d = x0 + (i+1)*h
             y_d = y + h*f(x,y)
             coords[i+1] = [x_d,y_d]

        return coords

def rk4_1order(f,x0,y0,n,bound):
     if n <= 0:
          raise ValueError("n must be greater than zero.")
     elif x0 > bound:
        raise ValueError("initial condition must be < than the inpunt bound!")
     coords = np.zeros((n+1,2))
     coords[0] = [x0,y0]
     h = (bound-x0) / n
     for i in range(n):
          x,y = coords[i]
             
          k1 = f(x,y)
          k2 = f(x+h/2, y+h/2*k1)
          k3 = f(x+h/2, y+h/2*k2)
          k4 = f(x+h, y+h*k3)

          x_d = x0 + (i+1)*h
          y_d = y + h * (k1+2*k2+2*k3+k4)/6
          coords[i+1] = [x_d,y_d]
        
     return coords
        

# Allows you to get the y-value from a specific x-value
# You can adjust the decimal places, note that rk4 is more accurate
def get_value(x,y,val,dec):
        function = interp1d(x,y,kind="cubic")
        num = np.round(function(val),dec)
        return num