import math
# -*- coding: utf-8 -*-

def get_coefficient(prompt):
    while True:
        try:
            coefficient = float(input(prompt))
            return coefficient
        except ValueError:
            print("Ошибка: введите число.")

def solve_equation(a, b, c):
    if a == 0:
        print("Ошибка: коэффициент A не может быть равен нулю.")
        return
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            print("Уравнение не имеет действительных корней.")
        elif d == 0:
            x = -b / (2 * a)
            print("Уравнение имеет один корень:", x)
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print("Уравнение имеет два корня:", x1, x2)

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
        except ValueError:
            print("Ошибка: коэффициенты должны быть числами.")
            a = get_coefficient("Введите коэффициент A: ")
            b = get_coefficient("Введите коэффициент B: ")
            c = get_coefficient("Введите коэффициент C: ")
    else:
        a = get_coefficient("Введите коэффициент A: ")
        b = get_coefficient("Введите коэффициент B: ")
        c = get_coefficient("Введите коэффициент C: ")

    solve_equation(a, b, c)


# Объектно-ориентированная реализация

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if self.a == 0:
            print("Ошибка: коэффициент A не может быть равен нулю.")
            return
        else:
            d = self.b ** 2 - 4 * self.a * self.c
            if d < 0:
                print("Уравнение не имеет действительных корней.")
            elif d == 0:
                x = -self.b / (2 * self.a)
                print("Уравнение имеет один корень:", x)
            else:
                x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
                x2 = (-self.b - math.sqrt(d)) / (2 * self.a)
                print("Уравнение имеет два корня:", x1, x2)

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
        except ValueError:
            print("Ошибка: коэффициенты должны быть числами.")
            a = float(input("Введите коэффициент A: "))
            b = float(input("Введите коэффициент B: "))
            c = float(input("Введите коэффициент C: "))
    else:
        a = float(input("Введите коэффициент A: "))
        b = float(input("Введите коэффициент B: "))
        c = float(input("Введите коэффициент C: "))

    equation = QuadraticEquation(a, b, c)
    equation.solve()
    