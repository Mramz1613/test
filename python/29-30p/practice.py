import turtle
import random


# number = int(input("Введите число чтобы получить его квадрат: "))
# def squear(enter):
#     return enter**2
#
#
# print(f"Ваше число: {squear(number)}")

# def list_func(a):
#     for i in range(len(a)):
#         print(a[i])
#
# string = "Я люблю Python"
# list_func(string)
#
# list = ["Я" "люблю" "Python"]
# list_func(string)

# def discrim(a,b,c):
#     D = b**2-4*a*c
#     return D
# a = float(input())
# b = float(input())
# c = float(input())
# res_D = discrim(a,b,c)
#
#
# def x1_x2():
#     x1 = (-b + (res_D ** 0.5)) / 2 * a
#     x2 = (-b - (res_D ** 0.5)) / 2 * a
#     return x1,x2
#
# def x1():
#     x = -(b/2*a)
#     return x
#
# if res_D > 0:
#     print(x1_x2())
# elif res_D == 0:
#     print(x1())
# elif res_D < 0:
#     print("У уравнения нет решений")
t = turtle
t.bgcolor("#ffffff")
t.speed(200)
color = ["red", "green", "blue", "black"]
def kvadrati():
    for i in range(40):
        x = random.randrange(0,t.window_width() // 2)
        y = random.randrange(0, t.window_height() // 2)
        size = (random.randint(100, 120))
        t.pencolor(random.choice(color))

        for a in range(size):
            t.forward(a*2)
            t.left(91)
            t.pu()
            t.setpos(-x,-y)
            t.pd()

        for b in range(size):
            t.forward(b*2)
            t.left(91)
            t.pu()
            t.setpos(x,y)
            t.pd()

        for c in range(size):
            t.forward(c*2)
            t.left(91)
            t.pu()
            t.setpos(-x,y)
            t.pd()

        for d in range(size):
            t.forward(d*2)
            t.left(91)
            t.pu()
            t.setpos(x,-y)
            t.pd()

for k in range(random.randint(10,100)):
    kvadrati()