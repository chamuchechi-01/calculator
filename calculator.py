

class Calculator:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


cal = Calculator()


class Calc(Calculator):
    pass


g = Calculator()


def Input():
    x = int(input("first number: "))
    y = int(input("second number"))
    return x, y


znak = input("viberite(+,-,*,/)")

if znak in ["+", "-", "*", "/"]:
    num1, num2 = Input()

    if znak == "+":
        print("result: ", g.add(num1, num2))
    if znak == "-":
        print("result: ", g.minus(num1, num2))
    if znak == "*":
        print("result: ", g.mult(num1, num2))
    if znak == "/":
        print("result: ", g.div(num1, num2))








