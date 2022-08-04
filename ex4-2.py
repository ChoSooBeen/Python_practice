import turtle as t

angle = 5
t.speed(0)
t.color('red')
t.pencolor('green')

for j in range(30):
    for i in range(angle):
        t. forward(100)
        t.right(360/angle)
    t.left(360/30)
t.mainloop()