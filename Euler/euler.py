import numpy as np

def euler(f, x0, y0, h, n):
    x = x0
    y = y0
    for _ in range(n):
        y = y + h * f(x, y)
        x = x + h

    return x, y

def f(x, y):
    return -2.0 * y

x_result, y_result = euler(f, 0.0, 1.0, 0.5, 1)

print(f'Error = {abs(y_result - np.exp(-2.0 * x_result))}')
