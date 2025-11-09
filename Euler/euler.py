import numpy as np
import matplotlib.pyplot as plt

def euler(f, x0, y0, h, n):
    x_vals = [x0]
    y_vals = [y0]
    x, y = x0, y0
    for _ in range(n):
        y = y + h * f(x, y)
        x = x + h
        x_vals.append(x)
        y_vals.append(y)

    return np.array(x_vals), np.array(y_vals)

def f(x, y):
    return -2.0 * y

def y_exact(x):
    return np.exp(-2.0 * x)

x0, y0 = 0.0, 1.0
h = 0.5
n = int(2.0 / h)

x_vals, y_vals = euler(f, x0, y0, h, n)

x_fine = np.linspace(0, 2, 1000)
y_fine = y_exact(x_fine)

plt.figure()
plt.plot(x_fine, y_fine, label='Exact solution')
plt.plot(x_vals, y_vals, label='Euler approximation')
plt.title("Euler's Method vs Exact Solution")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()