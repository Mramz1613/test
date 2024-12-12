import turtle as t
import random
newt = t.clone()
newt.lt(90)
class TreeType:
    def __init__(self,name,color,texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self,x,y):
        t.speed(100)
        t.setx(x)
        t.sety(y)
        t.color(self.color)
        t.begin_fill()
        t.pd()
        t.fd(30)
        t.right(90)
        t.bk(100)
        t.right(90)
        t.fd(30)
        t.right(90)
        t.bk(100)
        t.end_fill()
        t.pu()
        t.color(self.texture)
        t.goto(0+x,100+y)
        t.pd()
        for i in range(12):
            t.begin_fill()
            t.circle(20)
            t.end_fill()
            t.fd(8)
            t.rt(30)
            t.end_fill()
        t.up()
        t.goto(0,0)
        t.mainloop()

class Tree:
    def __init__(self,x,y,type:TreeType):
        self.x = x
        self.y = y
        self.type = type

    def draw(self):
        t.speed(100)
        t.setx(self.x)
        t.sety(self.y)
        t.color(self.type.color)
        t.begin_fill()
        t.pd()
        t.fd(30)
        t.right(90)
        t.bk(100)
        t.right(90)
        t.fd(30)
        t.right(90)
        t.bk(100)
        t.end_fill()
        t.pu()
        t.color(self.type.texture)
        t.goto(0+self.x ,100+self.y)
        t.pd()
        for i in range(12):
            t.begin_fill()
            t.circle(20)
            t.end_fill()
            t.fd(8)
            t.rt(30)
            t.end_fill()
        t.mainloop()


class TreeFactory:
    def __init__(self,treeType:TreeType):
        self.treeType = treeType

    def getTreeType(self):
        return self.treeType.color,self.treeType.name,self.treeType.texture

class Forest:
    def __init__(self,trees:Tree):
        self.trees = trees

    def plantTree(self,x,y,name,color,texture)->Tree:
        return Tree(x,y,TreeType(name,color,texture))

    def draw(self):
        for i in range(3):
            t.speed(100)
            t.setx(self.trees.x)
            t.sety(self.trees.y)
            t.color(self.trees.type.color)
            t.begin_fill()
            t.pd()
            t.fd(30)
            t.right(90)
            t.bk(100)
            t.right(90)
            t.fd(30)
            t.right(90)
            t.bk(100)
            t.end_fill()
            t.pu()
            t.color(self.trees.type.texture)
            t.goto(0+self.trees.x ,100+self.trees.y)
            t.pd()
            for i in range(12):
                t.begin_fill()
                t.circle(20)
                t.end_fill()
                t.fd(8)
                t.rt(30)
                t.end_fill()
            t.mainloop()

objTreeType2 = TreeType("sakura","black","pink")
objTreeType = TreeType("oak","brown","green")
objTree = Tree(0,0,objTreeType)
objTree2 = Tree(10,10,objTreeType2)
treelst = [objTree,objTree2]
objForest = Forest(objTree)
objForest.draw(




)
