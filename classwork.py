# a = {1,2,3,4,5,6,12,24}
# a.remove(12)
# print(a)


# a = {1,'Apple','jhon','CS','Mango','grapes'}
# a.update([2,3,4])
# print(a)


# a = {96,65,2,}
# b = {'joseph',1,'pedro',59}
# a.update(b)
# print(a)

# a = (input("write country name"))
# b = []
# print(f"you have " + a + " in your list")

# a = ["russia","uzb","france"]
# print(a)
# b = input("enter country for delete")
# if b in a:
#     a.remove(b)
#     print(f"{b}has been remowed")
# print("Updated list of countries:")
# print(a)

# def alphabet():
#     print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ")


# def number():
#     print("1,2,3,4,5,6,7,8,9,69") 


# def result():
#     a = int(input("chose only one 1 => alphabet, 0 => number"))
#     if a == 1:
#         alphabet()
#     if a == 0:
#         number()
# result()


# class tuning:
#     car = ("a")
#     a = input("pointer")
#     b = input("pointer")
#     def name(self):
#         print('my name is gigachad')
# p = tuning()
# print(p.car)
# print(p.b)
# print(p.a)
# p.name()



# class Myacedemy:
#     man = 10
#     def __init__(self,type,age,lang,emotion):
#         self.type = type
#         self.age = age
#         self.lang = lang
#         self.emotion = emotion

#     def __str__(self):
#         return f"{self.type}({self.age})({self.lang})({self.emotion})"

#     # def name(self):
#     #     print('My name is David')

# p = Myacedemy('man',35,'uz','mujik')
# c = Myacedemy('women',25,'ru','lox')
# f = Myacedemy('gigachad',10000,'??????','loshped')
# print(p.type)
# print(p.lang)
# print(c.age)
# print(p)
# print(c)
# print(f)



# from datetime import date

# class Bexruz:
     
#     def __init__(self,name,country,data_birth):
#         self.name =  name
#         self.country = country
#         self.data = data_birth


# b = Bexruz('Bexruz','tashkent',14)
# print(
#     "his name is" ,b.name,
#     "he was born in",b.country,
#     "he is ",b.data," years old"
# )
# print(b)



# from datetime import date

# class persons:

#     def __init__(self,name,country,data_of_birth,age):
#         self.name = name
#         self.country = country
#         self.data_of_birth = data_of_birth
#         self.age = age
    # def bexruz(self):
    #     self.name = 'Bexruz'
    #     self.country = "Tashkent"
    #     self.data_of_birth = 14
    #     return f"His name is,{self.name},He was born in "
    #     {self.country}
    #     "He is ", {self.data_of_birth}, " years old"
    #
    # def pet(self):
    #     self.name = 'Chixaxu'
    #     self.country = "Tashkent"
    #     self.data_of_birth = 1
    #     return f"His pets name is,{self.name},it was born in "
    #     {self.country}
    #     "it is ", {self.data_of_birth}, " years old"
    # def __init__(self,name,country,data_of_birth):
    #     self.name = name
    #     self.country = country
    #     self.data_of_birth = data_of_birth

# b = persons('ferdi','france',1962-7-12,60)
# a = persons('shweta maddox','canada',1982-10-20,40)
# c = persons('Elizaveta 2','uk',2000-1-1,20)
# b = BexruzFamily('')
# print(b.bexruz())
# print(b.pet())

# print("His name is ", a.name,
    #   "He was born in ", a.country,
#       "He was born at ",a.data_of_birth,
#       "he is ",b.age,"years old"
#      )


# print("His name is ", a.name,
#       "He was born in ", a.country,
#       "He was born at ",a.data_of_birth,
#       "he is ",a.age,"years old"
#      )

# print("His name is ", c.name,
#       "He was born in ", c.country,
#       "he was born at",c.data_of_birth,
#       "He is ",c.age,"years old")


# from datetime import date
# class Person:
#     def init(self,person,name,country,date_of_birth,age):
#          self.person=person
#          self.name=name
#          self.country=country
#          self.date_of_birth=date_of_birth
#          self.age=age
#     def str(self):
#         return f"{self.person}{self.name}{self.country}{self.date_of_birth}{self.age}"
# a=Person("Person1","\nFerdi ","\nfrance","\n1962-07-12","\n60")
# print(a)
# b=Person("Person2","\nshweta maddox","\ncanada","\n1982-10-20","\n40")
# print(b)
# c=Person("Person3","\nelizaveta 2","\nusa","\n2000-01-01","\n23")
# print(c)


# class Calculator:
#     def __init__(self):
#         pass

#     def add(self, x, y):
#         return x + y

#     def subtract(self, x, y):
#         return x - y

#     def multiply(self, x, y):
#         return x * y

#     def divide(self, x, y):
#             return x / y


# calc = Calculator()
# print("Addition: ", calc.add(5, 3))
# print("Subtraction: ", calc.subtract(5, 3))
# print("Multiplication: ", calc.multiply(5, 3))
# print("Division: ", calc.divide(6, 2))






# class lux_bus_ultra_turbo:

#     def __init__(self,name,milage,capacity):
#         self.name = name
#         self.milage = milage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100
    

# class vechicle(lux_bus_ultra_turbo):
#     pass


# a = lux_bus_ultra_turbo("president school",12,50)
# print("all cost:", a.fare())



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








