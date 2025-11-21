import numpy as np
import matplotlib.pyplot as plt

def rk4(f, x0, y0, h, n):
    x_vals = [x0]
    y_vals = [y0]
    x, y = x0, y0

    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + (h/2), y + (h/2) * k1)
        k3 = f(x + (h/2), y + (h/2) * k2)
        k4 = f(x + h, y + (h * k3))

        y = y + (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h

        x_vals.append(x)
        y_vals.append(y)
    
    return np.array(x_vals), np.array(y_vals)

def f(x, y):
    return -2.0 * y

def y_exact(x):
    return np.exp(-2.0 * x)

x0, y0 = 0.0, 1.0
h = 0.3
n = int(2.0 / h)

x_vals, y_vals = rk4(f, x0, y0, h, n)

x_fine = np.linspace(0, 2, 1000)
y_fine = y_exact(x_fine)

print(y_vals)
plt.figure()
plt.plot(x_fine, y_fine, 'red', label='Exact solution')
plt.plot(x_vals, y_vals, 'bo--', label='Runge Kutta approximation')
plt.title("Runge Kutta Method vs Exact Solution")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()