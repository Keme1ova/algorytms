# Метод оценивания с использованием квадратичной аппроксимации
# Метод Пауэлла
#   Метод Ньютона-Рафсона
#   Метод средней точки
#   Метод секущих

# 1
# Метод оценивания с использованием квадратичной аппроксимации
import math
import numpy as np
from scipy.optimize import minimize_scalar


def f(x):
    return math.sin(2*x) - x


def minimize(f, x0, d0, eps=1e-6, maxiter=100):
    x = x0
    d = np.array([d0])
    fx = f(x)
    for i in range(maxiter):
        # шаг 2
        def g(l):
            return f(x + l*d)
        lmin = minimize_scalar(g).x
        xprev = x
        x = x + lmin*d
        fxprev = fx
        fx = f(x)
        # шаг 3
        if abs(fx - fxprev) <= eps and abs(x - xprev) <= eps:
            return x
        # шаг 4
        if i > 0:
            if abs(fx - fxprev) > eps and abs(x - xprev) > eps:
                d1 = d
                d2 = x - xprev
                d = d2 / math.sqrt(d2.dot(d2))
                d = (d + d1) / math.sqrt((d + d1).dot(d + d1))
        # шаг 5
        if i == maxiter - 1:
            return x


# начальное приближение и направление
x0 = -0.5
d0 = 1.0

xmin = minimize(f, x0, d0)
print("Минимум функции:", xmin)


# 2
# Метод Пауэлла

def powell_method(f, x1, x2, eps=1e-6, dx=1e-4, max_iter=1000):
    x3 = x1 + 2 * dx
    f1, f2, f3 = f(x1), f(x2), f(x3)

    xmin = None
    for i in range(max_iter):
        if f1 > f2:
            x3 = x2 + 2 * dx
        else:
            x3 = x1 - dx
        f3 = f(x3)

        if f3 < f2:
            dx = 2 * dx * (x2 - x1) / (f2 - f3)
            x1, x2 = x2, x3
            f1, f2 = f2, f3
        else:
            dx = dx / 2
            x1, x2, x3 = x1, x2, x2
            f1, f2, f3 = f1, f2, f2

        x_min = (x1 + x2) / 2
        f_min = f(x_min)

        if xmin is None or f_min < f(xmin):
            xmin = x_min

        if abs(f_min - f(x_min + dx)) < eps and abs(xmin - x_min - dx) < eps:
            break

    return f_min, xmin


f = lambda x: x ** 2 - x + 2
x1, x2 = -1, 2
eps = 1e-7

min_val, min_point = powell_method(f, x1, x2, eps=eps)

print(f"Минимальная точка: {min_point}")








# 5
#   Метод секущих
def powell_method(f, x1, x2, eps=1e-6, dx=1e-4, max_iter=1000):
    x3 = x1 + 2 * dx
    f1, f2, f3 = f(x1), f(x2), f(x3)

    xmin = None
    for i in range(max_iter):
        if f1 > f2:
            x3 = x2 + 2 * dx
        else:
            x3 = x1 - dx
        f3 = f(x3)

        if f3 < f2:
            dx = 2 * dx * (x2 - x1) / (f2 - f3)
            x1, x2 = x2, x3
            f1, f2 = f2, f3
        else:
            dx = dx / 2
            x1, x2, x3 = x1, x2, x2
            f1, f2, f3 = f1, f2, f2

        x_min = (x1 + x2) / 2
        f_min = f(x_min)

        if xmin is None or f_min < f(xmin):
            xmin = x_min

        if abs(f_min - f(x_min + dx)) < eps and abs(xmin - x_min - dx) < eps:
            break

    return f_min, xmin


f = lambda x: x ** 2 - x + 2
x1, x2 = -1, 2
eps = 1e-7

min_val, min_point = powell_method(f, x1, x2, eps=eps)

print(f"Минимальная точка: {min_point}")