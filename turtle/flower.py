import turtle as t
import random

#꽃 색갈 채우기
def func_fillcolor():
    t.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.fillcolor(r, g, b)

    #꽃잎 하나 그리기
def func_leaf(size):
    for j in range(2):
        for i in range(15):
            t.forward(size)
            t.right(360/60)
        t.right(90)
    
#꽃 그리기
def func_flower(leafs, size):
    func_fillcolor()
    t.begin_fill()
    for k in range(leafs):
        func_leaf(size)
        t.right(360/leafs) 
    t.end_fill()      

#좌클릭시 실행하는 
def leftclick(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    leafs = random.randint(3, 8)
    size = random.randint(3, 10)
    func_flower(leafs, size)

t.speed(0)
t.shape('turtle')
t.pensize(2)

#꽃 그리기
t.onscreenclick(leftclick, 1)       
t.mainloop()
