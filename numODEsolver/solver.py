from scipy.interpolate import interp1d
import re
import numpy as np
from asteval import Interpreter


# get_function() -> Takes a function of x and y as an input. Make sure to use correct python syntax and put everything in curved brackets.
#   --> Example: numODEsolver.get_function("x+y"), The diff.eq. would then be: y' = x+y and it will be numerically solved for y.
class Solver:
     def __init__(self):
          self.aeval = Interpreter()
          self.aeval.symtable.pop("open", None)
     def get_function(self, func):
          expr = func.lower().replace("y'", "dy")
          f = self.aeval(f"lambda x, y, dy=0: {expr}")      
          if self.aeval.error or not callable(f):           
               msg = self.aeval.error[0].get_error() if self.aeval.error else "error"
               self.aeval.error = []
               raise ValueError(f"Could not parse function {func!r}: {msg}")

          def wrapped(x, y, dy=0):
               return f(x, y, dy)
          # order 2 if the expression depends on y' (dy), otherwise order 1
          wrapped.order = 2 if re.search(r"\bdy\b", expr) else 1
          return wrapped

     @staticmethod
     def _check_first_order(f):
          if getattr(f, "order", 1) == 2:
               raise ValueError("Function contains y' – use euler_2order or rk4_2order instead.")

     def euler_2order(self,f,x0,y0,dy0,n,bound): # euler cromer
          if n <= 0:
               raise ValueError("n must be greater than zero.")
          elif x0 >= bound:
               raise ValueError("initial condition must be < than the input bound!")
          vals = np.zeros((n+1,3))
          vals[0] = [x0,y0,dy0]
          h = (bound-x0)/n
          for i in range(n):
               x,y,dy = vals[i]

               dy_d = dy + h*f(x,y,dy)
               y_d = y + h * dy_d
               x_d = x0 + (i+1)*h
               vals[i+1] = [x_d,y_d,dy_d]

          return vals

     def euler_1order(self,f,x0,y0,n,bound):
          self._check_first_order(f)
          if n <= 0:
               raise ValueError("n must be greater than zero.")
          elif x0 >= bound:
               raise ValueError("initial condition must be < than the input bound!")
          vals = np.zeros((n+1, 2))
          vals[0] = [x0,y0]
          h = (bound-x0)/n
          for i in range(n):
               x,y = vals[i]
               x_d = x0 + (i+1)*h
               y_d = y + h*f(x,y)
               vals[i+1] = [x_d,y_d]

          return vals

     def rk4_1order(self,f,x0,y0,n,bound):
          self._check_first_order(f)
          if n <= 0:
               raise ValueError("n must be greater than zero.")
          elif x0 >= bound:
               raise ValueError("initial condition must be < than the input bound!")
          vals = np.zeros((n+1,2))
          vals[0] = [x0,y0]
          h = (bound-x0) / n
          for i in range(n):
               x,y = vals[i]
               
               k1 = f(x,y)
               k2 = f(x+h/2, y+h/2*k1)
               k3 = f(x+h/2, y+h/2*k2)
               k4 = f(x+h, y+h*k3)

               x_d = x0 + (i+1)*h
               y_d = y + h * (k1+2*k2+2*k3+k4)/6
               vals[i+1] = [x_d,y_d]

          return vals

     # y'' = f(x,y,y') is rewritten as a system of two first-order ODEs:
     #   y' = v,   v' = f(x,y,v)
     # and both equations are advanced together with classical RK4.
     def rk4_2order(self,f,x0,y0,dy0,n,bound):
          if n <= 0:
               raise ValueError("n must be greater than zero.")
          elif x0 >= bound:
               raise ValueError("initial condition must be < than the input bound!")
          vals = np.zeros((n+1,3))
          vals[0] = [x0,y0,dy0]
          h = (bound-x0) / n
          for i in range(n):
               x,y,v = vals[i]

               # k = slope of y (= v),  l = slope of v (= f)
               k1 = v
               l1 = f(x, y, v)
               k2 = v + h/2*l1
               l2 = f(x+h/2, y+h/2*k1, v+h/2*l1)
               k3 = v + h/2*l2
               l3 = f(x+h/2, y+h/2*k2, v+h/2*l2)
               k4 = v + h*l3
               l4 = f(x+h, y+h*k3, v+h*l3)

               x_d = x0 + (i+1)*h
               y_d = y + h * (k1+2*k2+2*k3+k4)/6
               v_d = v + h * (l1+2*l2+2*l3+l4)/6
               vals[i+1] = [x_d,y_d,v_d]

          return vals

     # You can adjust the decimal places, note that rk4 is more accurate
     def get_value(self,data,val,dec):
          x_vals = data[:,0]
          y_vals = data[:,1]
          function = interp1d(x_vals,y_vals,kind="cubic")
          num = np.round(function(val),dec)
          return num