from math import exp

def f(x: float, u: float, v: float) -> float:
    return exp(x) * (1 + x ** 2) + u - v

def g(x: float, u: float, v: float) -> float:
    return x * exp(x) + u + v

def step(x: float, u: float, v: float, h: float) -> tuple[float]:
    phi_0 = h * f(x, u, v)
    xi_0 = h * g(x, u, v)

    phi_1 = h * f(x + h / 2, u + phi_0 / 2, v + xi_0 / 2)
    xi_1 = h * g(x + h / 2, u + phi_0 / 2, v + xi_0 / 2)

    phi_2 = h * f(x + h / 2, u + phi_1 / 2, v + xi_1 / 2)
    xi_2 = h * g(x + h / 2, u + phi_1 / 2, v + xi_1 / 2)

    phi_3 = h * f(x + h, u + phi_2, v + xi_2)
    xi_3 = h * g(x + h, u + phi_2, v + xi_2)

    u += (phi_0 + 2 * phi_1 + 2 * phi_2 + phi_3) / 6
    v += (xi_0 + 2 * xi_1 + 2 * xi_2 + xi_3) / 6

    return u, v

def jump(x: float, u: float, v: float, h: float, e: float) -> tuple[float]:
    u0, v0 = step(x, u, v, h)

    while True:
        u1, v1 = step(x, u, v, h / 2)
        u2, v2 = step(x + h / 2, u1, v1, h / 2)

        if abs(u0 - u2) < e and abs(v0 - v2) < e:
            break
        else:
            u0, v0 = u1, v1
            h /= 2
    
    return u2, v2, h

def runge_kutta(a: float, b: float, u: float, v: float, h_start: float, e: float) -> tuple[float, float]:
    e *= 15/16
    x = a

    while x < b:
        u0, v0, h = jump(x, u, v, h_start, e)

        if x + h_start > b:
            h_start = b - x
            continue

        u, v = u0, v0
        x += h

    return u, v
