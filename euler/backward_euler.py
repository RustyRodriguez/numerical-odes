import numpy as np
import matplotlib.pyplot as plt

def backward_euler(f, x0, y0, h, n):
    x_vals = [x0]
    y_vals = [y0]
    x, y = x0, y0

    for _ in range(n):

        y = y / (1 + (2 * h))
        x = x + h
        x_vals.append(x)
        y_vals.append(y)

    return np.array(x_vals), np.array(y_vals)

def y_exact(x): 
    return np.exp(-2 * x)

x0 = 0.0
y0 = 1.0
h = 0.5 
n = int(2.0 / h)

x_vals, y_vals = backward_euler(lambda x, y: -2*y, x0, y0, h, n)

x_exact = np.linspace(0, 2, 200)
y_exact = y_exact(x_exact)

plt.figure()
plt.plot(x_exact, y_exact, 'k', label='Exact $e^{-2x}$')
plt.plot(x_vals, y_vals, 'bo--', label='Backward Euler')
plt.title("Backward Euler (Implicit) vs Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
