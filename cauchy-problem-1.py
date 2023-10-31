from math import exp

def f(x: float, y: float) -> float:
    return exp(x) + y

def step(x: float, y: float, h: float) -> float:
    phi_0 = h * f(x, y)
    phi_1 = h * f(x + h / 2, y + phi_0 / 2)
    phi_2 = h * f(x + h / 2, y + phi_1 / 2)
    phi_3 = h * f(x + h, y + phi_2)

    return y + (phi_0 + 2 * phi_1 + 2 * phi_2 + phi_3) / 6

def jump(x: float, y: float, h: float, e: float) -> tuple[float]:
    y0 = step(x, y, h)

    while True:
        y1 = step(x, y, h/2)
        y2 = step(x + h/2, y1, h/2)

        if abs(y0 - y2) < e:
            break
        else:
            h /= 2
            y0 = y1

    return y2, h

if __name__ == "__main__":
    a = float(input("Левый конец отрезка: "))
    b = float(input("Правый конец отрезка: "))
    print("")
    
    y = float(input(f"Значение функции y(x) в точке {a}: "))
    print("")

    e = float(input("Точность: "))
    h_start = float(input("Стартовый шаг: "))

    e *= 15/16
    x = a

    while x < b:        
        y0, h = jump(x, y, h_start, e)

        if x + h_start > b:
            h_start = b - x
            continue
        
        y = y0
        x += h

        print("\n----------\n")

        print(f"x = {x}")
        print("")

        y_true = x * exp(x)
      
        print(f"Приближенное y(x) = {y}")
        print(f"    Истинное y(x) = {y_true}")

        print("")

        print(f"Шаг: {h}")
        print(f"Погрешность: {abs(y_true - y)}")
