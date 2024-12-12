# m = "Бла Бла Бла"
# print(m.rfind('а'))
# listM = m.count(" ")
# listM.clear()
# for i in range(11):
#     listM.append(i)
# typeM = list(map(type(str),listM))
# print(typeM)
import turtle as t
def sq(x:int,y:int):
    t.color("#000000")
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.onclick(click())


def click():
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.mainloop()


sq(0,0)