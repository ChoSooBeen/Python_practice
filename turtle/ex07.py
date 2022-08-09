#거북이 경주 프로그램
import turtle as t
import random
import time

t.speed(0)
t.penup()
t.goto(-140, 140)

# 경주에 필요한 경주라인 그리기
for i in range(16):
    t.write(i, align='center')
    t.right(90)
    t.forward(10)
    t.pendown()
    t.forward(150)
    t.penup()
    t.backward(160)
    t.left(90)
    t.forward(20)

finish_line = t.xcor() - 20

#4마리 거북이 준비
t_color = ['red', 'yellow', 'green', 'blue']
t_list = []

for i in range(len(t_color)):
    tt = t.Turtle()
    tt.color(t_color[i])
    tt.shape('turtle')
    tt.penup()
    tt.goto(-160, 150-40*(i+1))
    tt.pendown()
    t_list.append(tt)

#모든 거북이가 달리는 함수
def run():
    while True:
        for i in t_list:
            i.forward(random.randint(1,5))
            if i.xcor() >= finish_line: #가장 처음 결승선에 도착한 거북이 return
                return i

winner =run()

#세레머니
for i in range(1, 6):
    winner.shapesize(i,i)
    time.sleep(0.1)
winner.right(random.randint(1, 360))

t.mainloop()