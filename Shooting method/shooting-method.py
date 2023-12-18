import cauchy
import bisection

from math import exp

#def u(x: float) -> float:
#    return x * exp(x)

#def v(x: float) -> float:
#    return x ** 2 * exp(x)

def f(x: float, u: float, v: float) -> float:
    return exp(x) * (1 + x ** 2) + u - v

def g(x: float, u: float, v: float) -> float:
    return x * exp(x) + u + v

if __name__ == "__main__":
    cauchy.f = f
    cauchy.g = g

    a = float(input("Левый конец отрезка: "))
    b = float(input("Правый конец отрезка: "))

    print("")

    alpha_0 = float(input("Значение α0: "))
    beta_0 = float(input("Значение β0: "))
    gamma_0 = float(input("Значение γ0: "))

    print("")

    alpha_1 = float(input("Значение α1: "))
    beta_1 = float(input("Значение β1: "))
    gamma_1 = float(input("Значение γ1: "))

    print("")

    ksi = float(input("Значение ξ: "))
    epsilon = float(input("Точность: "))

    print("")

    def F(ksi: float) -> float:
        u, v = cauchy.runge_kutta(a, b, ksi, (gamma_0 - alpha_0 * ksi) / beta_0, 0.3, epsilon)
        return alpha_1 * u + beta_1 * v - gamma_1
    
    ksi = bisection.bisection(-abs(ksi) - 1, abs(ksi) + 1, F, epsilon)
    x = a

    while x < b:
        u, v = cauchy.runge_kutta(a, x, ksi, (gamma_0 - alpha_0 * ksi) / beta_0, 0.3, epsilon)
        print(f"X = {x}; U(X) = {u}; V(X) = {v}")

        x += 0.1
