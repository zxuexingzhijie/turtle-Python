import turtle
import time
import random
q = turtle.Turtle()
t = turtle.Turtle()
u = turtle.Turtle()
yy = turtle.Turtle()
d = turtle.Turtle()
h = turtle.Turtle()
lh = turtle.Turtle()
f = turtle.Turtle()
bl = turtle.Turtle()
yu = turtle.Turtle()

t.hideturtle()
u.hideturtle()
yy.hideturtle()
d.hideturtle()
h.hideturtle()
lh.hideturtle()
f.hideturtle()
bl.hideturtle()
yu.hideturtle()
# t.speed(0)
s = turtle.Screen()

q.shape('circle')
q.up()
q.goto(-15,-60)
q.down()
# 背景
s.setup(860, 600)
s.bgcolor("#022C4F")

s.tracer(0)

def move(x,y):
    q.up()
    q.goto(x,y)
    q.down()
    

q.pencolor("#056BBF")
move(-230, -20)
q.write("暴风雨即将来临......", font=("华文行楷", 37))

# 海
def peng(x,y):
    s.bgcolor("black")
    q.hideturtle()
    q.clear()
    h.up()
    h.goto(-450,-225)
    h.down()
    h.pensize(200)
    h.pencolor('#01063A')
    h.forward(1000)
    h.setheading(90)
    h.forward(100)
    h.setheading(180)
    h.forward(1000)
    h.setheading(90)
    h.forward(50)
    h.setheading(0)
    h.forward(1000)

    h.pencolor('black')
    h.pensize(3)

    def lang():    
        h.forward(50)
        h.left(165)
        h.pencolor('#05035D')
        h.pensize(5)
        h.forward(70)
        h.backward(70)
        h.right(165)
        h.pencolor('black')
        
        h.pensize(3)
        h.backward(50)
        h.right(2)
        h.forward(60)
        h.right(-178)
        h.forward(60)
        h.right(2)
        h.backward(50)
        h.forward(60)
        h.right(30)
        h.forward(30)
        h.backward(20)
        h.left(8)
        h.forward(15)
        h.right(6)
        h.backward(20)
        
        h.pensize(5)
        
        h.left(8)
        h.forward(25)
        h.circle(25, 25)
        h.pensize(2)
        h.left(20)
        h.forward(15)
        h.right(6)
        h.backward(20)
        
        h.pensize(3)
        
        h.forward(25)
        s.update()
    def langh():    
        lh.forward(50)
        lh.left(165)
        lh.pencolor('#05035D')
        lh.pensize(5)
        lh.forward(70)
        lh.backward(70)
        lh.right(165)
        lh.pencolor('black')
        
        lh.pensize(3)
        lh.backward(50)
        lh.right(2)
        lh.forward(60)
        lh.right(-178)
        lh.forward(60)
        lh.right(2)
        lh.backward(50)
        lh.forward(60)
        lh.right(30)
        lh.forward(30)
        lh.backward(20)
        lh.left(8)
        lh.forward(15)
        lh.right(6)
        lh.backward(20)
        
        lh.pensize(5)
        
        lh.left(8)
        lh.forward(25)
        lh.circle(25, 25)
        lh.pensize(2)
        lh.left(20)
        lh.forward(15)
        lh.right(6)
        lh.backward(20)
        
        lh.pensize(3)
        
        lh.forward(25)
        s.update()
    for i in range(100):
        l = random.randint(-430, 430)
        hl = random.randint(-300, 0)
        bw = random.randint(0, 20)
        h.up()
        h.goto(l,hl)
        h.down()
        h.setheading(0)
        h.right(bw)
        lang()
    for i in range(15):
        l = random.randint(-400, 400)
        hl = random.randint(-300, 0)
        bw = random.randint(5,25)
        h.up()
        h.goto(l,hl)
        h.down()
        h.setheading(0)
        h.right(bw)
        h.pensize(8)
        h.forward(30)
        h.right(3)
        h.backward(30)
        h.left(10)
        h.forward(30)
        h.right(20)
        h.backward(30)
        h.right(150)
        h.forward(30)
        h.left(160)
        h.forward(80)
    for i in range(200):
        l = random.randint(-400, 400)
        hl = random.randint(-300, 0)
        bw = random.randint(0,20)
        h.up()
        h.goto(l,hl)
        h.down()
        h.setheading(0)
        h.right(bw)
        h.pensize(3)
        h.forward(15)
        s.update()
    for i in range(150):
        l = random.randint(-400, 400)
        hl = random.randint(-10, 20)
        bw = random.randint(0,20)
        h.up()
        h.goto(l,hl)
        h.down()
        h.setheading(0)
        h.right(bw)
        h.pensize(2)
        h.forward(15)
        s.update()
    h.up()
    h.goto(-430,23)
    h.down()
    h.setheading(0)
    h.pensize(5)
    h.forward(1000)
    h.up()
    h.goto(-225,18)
    h.down()
    h.pensize(5)
    h.forward(1000)

    d.up()
    d.goto(-100,-85)
    d.down()
    d.begin_fill()
    d.circle(1000, 8)
    d.circle(1000, -11)
    d.circle(1000, 11)
    d.circle(3, 165)
    d.circle(1000, 12)
    d.circle(4000, 2)
    d.setheading(0)
    d.right(1.5)
    d.forward(180)
    d.fillcolor("#413C3C")
    d.end_fill()
    d.up()

    # 树
    def shuu(p,q,o,w):    
        u.up()
        u.goto(-90,-70)
        u.down()
        u.pencolor('#0B0B0B')
        u.pensize(3)
        u.setheading(87)
        u.forward(15)
        u.right(13)
        u.pensize(4)
        u.backward(25)
        u.setheading(0)
        u.pensize(5)
        u.forward(7)
        u.up()
        u.goto(-90,-70)
        u.down()
        u.setheading(87)
        u.forward(35)
        u.right(15)
        u.forward(30)
        u.right(12)
        u.forward(30)
        u.backward(20)
        u.left(18) 
        u.forward(30)
        u.backward(30)
        u.right(18)
        u.backward(10)
        u.left(12) 
        u.backward(20)
        u.left(18) 
        u.forward(50)
        u.backward(20)
        u.right(17)
        u.forward(40)
        u.backward(20)
        u.left(18) 
        u.forward(35)
        u.up()
        u.goto(-90,-70)
        u.down()
        u.setheading(97)
        u.forward(35)
        u.left(5) 
        u.forward(50)
        u.backward(15)
        u.right(17)
        u.forward(35)
        u.up()
        u.goto(-90,-70)
        u.down()
        u.setheading(97)
        u.forward(35)
        u.left(5) 
        u.forward(5)
        u.left(25) 
        u.forward(55)
        u.backward(20)
        u.right(25) 
        u.forward(40)
        u.backward(15)
        u.right(25) 
        u.forward(35)
        u.backward(35)
        u.left(50)
        u.forward(25)
        u.backward(25)
        u.up()
        u.goto(-90,-70)
        u.down()
        u.setheading(-90)
        u.forward(5)
        u.up()
        u.goto(-90,-70)
        u.down()
        u.setheading(97)
        u.forward(35)
        u.left(5) 
        u.forward(25)
        u.pensize(1)
        u.right(45) 
        u.forward(35)
        u.left(15) 
        u.backward(45)
        u.left(50) 
        u.forward(35)
        u.up()
        u.goto(-90,-70)
        u.down()
        u.setheading(97)
        u.forward(35)
        u.left(5) 
        u.forward(5)
        u.left(25) 
        u.forward(20)
        u.left(20) 
        u.forward(35)

        for i in range(350):

            u.pencolor("#292525")
            x = random.randint(p, q)
            y = random.randint(o, w+15)
            if p<=x<=p+20 and o<=y<=o+15:
                continue
            elif q-20<=x<=q and o<=y<=o+15:
                continue
            elif p<=x<=p+20 and w-15<=y<=w:
                continue
            elif q-20<=x<=q and w-15<=y<=w:
                continue
            
            elif p<=x<=p+40 and w<=y<=w+15:
                continue
            elif q-40<=x<=q and w<=y<=w+15:
                continue
            u.up()
            u.goto(x,y)
            u.down()
            u.pensize(2)
            u.right(30)
            u.forward(7)
            u.right(150)
            u.forward(7)
            u.right(random.randint(30, 150))
            s.update()

        
    u.up()
    u.goto(-90,-70)
    u.down()
    shuu(-60-90,60-90,40-70,135-70)

    def Hua(xh,yh):
        f.pencolor("#292525")
        f.up()
        f.goto(xh,yh)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh,yh)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh,yh)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh,yh)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh,yh)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        
        # s.update()    
    def Hua2(xh2,yh2):
        f.up()
        f.goto(xh2,yh2)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh2,yh2)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh2,yh2)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh2,yh2)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh2,yh2)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        # s.update()
    def Hua3(xh3,yh3):
        f.up()
        f.goto(xh3,yh3)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh3,yh3)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh3,yh3)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh3,yh3)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh3,yh3)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        # s.update()
    def Hua4(xh4,yh4):
        f.up()
        f.goto(xh4,yh4)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh4,yh4)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh4,yh4)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh4,yh4)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh4,yh4)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        # s.update()
    def Hua5(xh5,yh5):
        f.up()
        f.goto(xh5,yh5)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh5,yh5)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh5,yh5)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh5,yh5)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        f.up()
        f.goto(xh5,yh5)
        f.down()
        f.pensize(2)
        f.setheading(0)
        f.right(30)
        f.forward(7)
        f.right(150)
        f.forward(7)
        # s.update()

    # 变量与概率
    a7=0
    b7=0
    c7=0
    d7=0
    a8=0
    b8=0 
    c8=0
    d8=0
    a9=0
    b9=0
    c9=0
    d9=0

    probability0=[0,0,0,0,1,1]
    probability1=[0,0,0,0,1,1,1]
    probability2=[0,0,1,1,1,1,1]
    probability3=[0,0,0,0,1,1]
    probability4=[0,0,0,1,1]
    probability5=[0,0,0,1,1]
    probability6=[0,1,1,1,1,1,1,1,1]
    probability7=[1,1,1]
    probability10=[0,0,0,0]
    shanv=[0,0,0,1,1,1,1,1,1]
    shanvz=[0,0,0,0,1,1,1]
    shanvz2=[0,0,0,0,0,0,1]
    shanvz3=[0,0,0,0,0,0,1]

    # 雷电
    def leidian():    
        x = random.randint(-200, 200)
        t.up()
        t.goto(x,370)
        t.setheading(-45)
        t.down()
        ld2 = random.choice(probability10)    
        s.bgcolor('white')
        # time.sleep(0.1)
        s.bgcolor('#100F0F')
        shan = random.choice(shanv)
        shanz = random.choice(shanvz)
        shanz2 = random.choice(shanvz2)
        shanz3 = random.choice(shanvz3)
        if shan==0:
            time.sleep(0.2)
            s.bgcolor('white')
            time.sleep(0.1)
            s.bgcolor('#100F0F')

        for i in range(10):       
            a = random.randint(50, 80)
            b = random.randint(10, 45)
            c = random.randint(50, 80)
            d = random.randint(5, 7)
            t.pencolor("white")
            t.pensize(d)
            t.right(a)
            t.forward(b)
            
            bt = random.choice(probability0)
            
            if bt==0:
                t.pencolor("white")
                bt1 = random.choice(probability1)
                bt2 = random.choice(probability2)
                bt3 = random.choice(probability3)
                bt4 = random.choice(probability4)
                bt5 = random.choice(probability5)
                bt6 = random.choice(probability6)
                bt7 = random.choice(probability7)
                atz = random.randint(10, 30)
                btz = random.randint(10, 45)
                ctz = random.randint(10, 30)
                dtz = random.randint(1, 2)
                t.pensize(dtz)
                t.right(atz)
                t.forward(btz)
                t.left(ctz)
                t.forward(btz)
                btz1=btz
                atz1=atz 
                ctz1=ctz 
                dtz1=dtz
                def sss(btz1,atz1,ctz1,dtz1):
                    t.pensize(dtz1)
                    t.forward(btz1)
                    t.right(ctz1)
                    t.forward(btz1)
                    t.left(atz1)
                if bt1==0:
                    atz = random.randint(10, 30)
                    btz = random.randint(10, 45)
                    ctz = random.randint(10, 30)
                    dtz = random.randint(1, 2)
                    t.pensize(dtz)
                    t.right(atz)
                    t.forward(btz)
                    t.left(ctz)
                    t.forward(btz)
                    btz2=btz
                    atz2=atz 
                    ctz2=ctz 
                    dtz2=dtz
                    if bt2==0:
                        atz = random.randint(10, 30)
                        btz = random.randint(10, 45)
                        ctz = random.randint(10, 30)
                        dtz = random.randint(1, 2)
                        t.pensize(dtz)
                        t.right(atz)
                        t.forward(btz)
                        t.left(ctz)
                        t.forward(btz)
                        btz3=btz
                        atz3=atz 
                        ctz3=ctz 
                        dtz3=dtz
                        if bt3==0:
                            atz = random.randint(10, 30)
                            btz = random.randint(10, 45)
                            ctz = random.randint(10, 30)
                            dtz = random.randint(1, 2)
                            t.pensize(dtz)
                            t.right(atz)
                            t.forward(btz)
                            t.left(ctz)
                            t.forward(btz)
                            btz4=btz
                            atz4=atz 
                            ctz4=ctz 
                            dtz4=dtz
                            if bt4==0:
                                atz = random.randint(10, 30)
                                btz = random.randint(10, 45)
                                ctz = random.randint(10, 30)
                                dtz = random.randint(1, 2)
                                t.pensize(dtz)
                                t.right(atz)
                                t.forward(btz)
                                t.left(ctz)
                                t.forward(btz)
                                btz5=btz
                                atz5=atz 
                                ctz5=ctz 
                                dtz5=dtz
                                if bt5==0:
                                    atz = random.randint(10, 30)
                                    btz = random.randint(10, 45)
                                    ctz = random.randint(10, 30)
                                    dtz = random.randint(1, 2)
                                    t.pensize(dtz)
                                    t.right(atz)
                                    t.forward(btz)
                                    t.left(ctz)
                                    t.forward(btz)
                                    btz6=btz
                                    atz6=atz 
                                    ctz6=ctz 
                                    dtz6=dtz
                                    if bt6==0:
                                        atz = random.randint(10, 30)
                                        btz = random.randint(10, 45)
                                        ctz = random.randint(10, 30)
                                        dtz = random.randint(1, 2)
                                        t.pensize(dtz)
                                        t.right(atz)
                                        t.forward(btz)
                                        t.left(ctz)
                                        t.forward(btz)
                                        btz7=btz
                                        atz7=atz 
                                        ctz7=ctz 
                                        dtz7=dtz
                                        t.right(180)
                                        sss(btz7,atz7,ctz7,dtz7)
                                        sss(btz6,atz6,ctz6,dtz6)
                                        sss(btz5,atz5,ctz5,dtz5)
                                        sss(btz4,atz4,ctz4,dtz4)
                                        sss(btz3,atz3,ctz3,dtz3)
                                        sss(btz2,atz2,ctz2,dtz2)
                                        sss(btz1,atz1,ctz1,dtz1)
                                        t.right(180)
                                    if bt6==1:
                                        t.right(180)
                                        sss(btz6,atz6,ctz6,dtz6)
                                        sss(btz5,atz5,ctz5,dtz5)
                                        sss(btz4,atz4,ctz4,dtz4)
                                        sss(btz3,atz3,ctz3,dtz3)
                                        sss(btz2,atz2,ctz2,dtz2)
                                        sss(btz1,atz1,ctz1,dtz1)
                                        t.right(180)
                                if bt5==1:
                                    t.right(180)
                                    sss(btz5,atz5,ctz5,dtz5)
                                    sss(btz4,atz4,ctz4,dtz4)
                                    sss(btz3,atz3,ctz3,dtz3)
                                    sss(btz2,atz2,ctz2,dtz2)
                                    sss(btz1,atz1,ctz1,dtz1)
                                    t.right(180)
                            if bt4==1:
                                t.right(180)
                                sss(btz4,atz4,ctz4,dtz4)
                                sss(btz3,atz3,ctz3,dtz3)
                                sss(btz2,atz2,ctz2,dtz2)
                                sss(btz1,atz1,ctz1,dtz1)
                                t.right(180)
                        if bt3==1:
                            t.right(180)
                            sss(btz3,atz3,ctz3,dtz3)
                            sss(btz2,atz2,ctz2,dtz2)
                            sss(btz1,atz1,ctz1,dtz1)
                            t.right(180)
                    if bt2==1:
                        t.right(180)
                        sss(btz2,atz2,ctz2,dtz2)
                        sss(btz1,atz1,ctz1,dtz1)
                        t.right(180)
                if bt1==1:
                    t.right(180)
                    sss(btz1,atz1,ctz1,dtz1)
                    t.right(180)
            t.pensize(d)
            t.left(c)
            t.forward(b)
            bt = random.choice(probability0)
            if bt==0:
                t.pencolor("white")
                bt1 = random.choice(probability1)
                bt2 = random.choice(probability2)
                bt3 = random.choice(probability3)
                bt4 = random.choice(probability4)
                bt5 = random.choice(probability5)
                bt6 = random.choice(probability6)
                bt7 = random.choice(probability7)
                atz = random.randint(10, 30)
                btz = random.randint(10, 45)
                ctz = random.randint(10, 30)
                dtz = random.randint(1, 2)
                t.pensize(dtz)
                t.left(ctz)
                t.forward(btz)
                t.right(atz)
                t.forward(btz)
                btz1=btz
                atz1=atz 
                ctz1=ctz 
                dtz1=dtz
                def sss(btz1,atz1,ctz1,dtz1):
                    t.pensize(dtz1)
                    t.forward(btz1)
                    t.left(atz1)
                    t.forward(btz1)
                    t.right(ctz1)
                if bt1==0:
                    atz = random.randint(10, 30)
                    btz = random.randint(10, 45)
                    ctz = random.randint(10, 30)
                    dtz = random.randint(1, 2)
                    t.pensize(dtz)
                    t.left(ctz)
                    t.forward(btz)
                    t.right(atz)
                    t.forward(btz)
                    btz2=btz
                    atz2=atz 
                    ctz2=ctz 
                    dtz2=dtz
                    if bt2==0:
                        atz = random.randint(10, 30)
                        btz = random.randint(10, 45)
                        ctz = random.randint(10, 30)
                        dtz = random.randint(1, 2)
                        t.pensize(dtz)
                        t.left(ctz)
                        t.forward(btz)
                        t.right(atz)
                        t.forward(btz)
                        btz3=btz
                        atz3=atz 
                        ctz3=ctz 
                        dtz3=dtz
                        if bt3==0:
                            atz = random.randint(10, 30)
                            btz = random.randint(10, 45)
                            ctz = random.randint(10, 30)
                            dtz = random.randint(1, 2)
                            t.pensize(dtz)
                            t.left(ctz)
                            t.forward(btz)
                            t.right(atz)
                            t.forward(btz)
                            btz4=btz
                            atz4=atz 
                            ctz4=ctz 
                            dtz4=dtz
                            if bt4==0:
                                atz = random.randint(10, 30)
                                btz = random.randint(10, 45)
                                ctz = random.randint(10, 30)
                                dtz = random.randint(1, 2)
                                t.pensize(dtz)
                                t.left(ctz)
                                t.forward(btz)
                                t.right(atz)
                                t.forward(btz)
                                btz5=btz
                                atz5=atz 
                                ctz5=ctz 
                                dtz5=dtz
                                if bt5==0:
                                    atz = random.randint(10, 30)
                                    btz = random.randint(10, 45)
                                    ctz = random.randint(10, 30)
                                    dtz = random.randint(1, 2)
                                    t.pensize(dtz)
                                    t.left(ctz)
                                    t.forward(btz)
                                    t.right(atz)
                                    t.forward(btz)
                                    btz6=btz
                                    atz6=atz 
                                    ctz6=ctz 
                                    dtz6=dtz
                                    if bt6==0:
                                        atz = random.randint(10, 30)
                                        btz = random.randint(10, 45)
                                        ctz = random.randint(10, 30)
                                        dtz = random.randint(1, 2)
                                        t.pensize(dtz)
                                        t.left(ctz)
                                        t.forward(btz)
                                        t.right(atz)
                                        t.forward(btz)
                                        btz7=btz
                                        atz7=atz 
                                        ctz7=ctz 
                                        dtz7=dtz
                                        t.right(180)
                                        sss(btz7,atz7,ctz7,dtz7)
                                        sss(btz6,atz6,ctz6,dtz6)
                                        sss(btz5,atz5,ctz5,dtz5)
                                        sss(btz4,atz4,ctz4,dtz4)
                                        sss(btz3,atz3,ctz3,dtz3)
                                        sss(btz2,atz2,ctz2,dtz2)
                                        sss(btz1,atz1,ctz1,dtz1)
                                        t.right(180)
                                    if bt6==1:
                                        t.right(180)
                                        sss(btz6,atz6,ctz6,dtz6)
                                        sss(btz5,atz5,ctz5,dtz5)
                                        sss(btz4,atz4,ctz4,dtz4)
                                        sss(btz3,atz3,ctz3,dtz3)
                                        sss(btz2,atz2,ctz2,dtz2)
                                        sss(btz1,atz1,ctz1,dtz1)
                                        t.right(180)
                                if bt5==1:
                                    t.right(180)
                                    sss(btz5,atz5,ctz5,dtz5)
                                    sss(btz4,atz4,ctz4,dtz4)
                                    sss(btz3,atz3,ctz3,dtz3)
                                    sss(btz2,atz2,ctz2,dtz2)
                                    sss(btz1,atz1,ctz1,dtz1)
                                    t.right(180)
                            if bt4==1:
                                t.right(180)
                                sss(btz4,atz4,ctz4,dtz4)
                                sss(btz3,atz3,ctz3,dtz3)
                                sss(btz2,atz2,ctz2,dtz2)
                                sss(btz1,atz1,ctz1,dtz1)
                                t.right(180)
                        if bt3==1:
                            t.right(180)
                            sss(btz3,atz3,ctz3,dtz3)
                            sss(btz2,atz2,ctz2,dtz2)
                            sss(btz1,atz1,ctz1,dtz1)
                            t.right(180)
                    if bt2==1:
                        t.right(180)
                        sss(btz2,atz2,ctz2,dtz2)
                        sss(btz1,atz1,ctz1,dtz1)
                        t.right(180)
                if bt1==1:
                    t.right(180)
                    sss(btz1,atz1,ctz1,dtz1)
                    t.right(180)
            time.sleep(0.01)
            if i==3:
                if shanz==0:
                    s.bgcolor('white')
                    time.sleep(0.1)
                    s.bgcolor('#100F0F')
            if i==5:
                if shanz2==0:
                    s.bgcolor('white')
                    time.sleep(0.1)
                    s.bgcolor('#100F0F')
            if i==7:
                if shanz3==0:
                    s.bgcolor('white')
                    time.sleep(0.1)
                    s.bgcolor('#100F0F')
                    
            s.bgcolor('white')
            time.sleep(0.1)
            s.bgcolor('#100F0F')

        s.bgcolor('white')
        time.sleep(0.1)
        s.bgcolor('#100F0F')
        time.sleep(0.2)
        s.bgcolor('white')
        time.sleep(0.1)
        s.bgcolor('#100F0F')

    # 雨
    def yus(a,b):    
        yy.up()
        yy.goto(a,b)
        yy.down()
        yy.pensize(1)
        yy.forward(20)
        
    for i in range(66):
        if i%5==0:    
            xh = random.randint(-65,35)
            yh = random.randint(-60,30)
            xh2 = random.randint(-65,35)
            yh2 = random.randint(-60,30)
            xh3 = random.randint(-65,35)
            yh3 = random.randint(-60,30)
            xh4 = random.randint(-65,35)
            yh4 = random.randint(-60,30)
            xh5 = random.randint(-65,35)
            yh5 = random.randint(-60,30)
        Hua(xh,yh)
        Hua2(xh2,yh2)
        Hua3(xh3,yh3)
        Hua4(xh4,yh4)
        Hua5(xh5,yh5)

        
        if i%2==0:    
            for v in range(5):
                yy.setheading(-45)
                yy.pencolor("#5F5E5E")
                yy.clear()
                if i==20: 
                    yy.clear()
                    s.bgcolor('white')
                    time.sleep(0.1)
                    s.bgcolor('#100F0F')
                    leidian()
                    break
                if i==24:
                    t.clear()
                if i==40: 
                    f.clear()
                    yy.clear()
                    s.bgcolor('white')
                    time.sleep(0.1)
                    s.bgcolor('#100F0F')
                    leidian()
                    break
                if i==44:
                    t.clear()
                if i==60:
                    f.clear()
                    yy.clear()
                    s.bgcolor('white')
                    time.sleep(0.1)
                    s.bgcolor('#100F0F')
                    leidian()
                    break
                if i==64:
                    t.clear()
                if i==80: 
                    f.clear()
                    yy.clear()
                    s.bgcolor('white')
                    time.sleep(0.1)
                    s.bgcolor('#100F0F')
                    leidian()
                    break
                if i==84:
                    t.clear()
                for p in range(50):
                    a=random.randint(-300, 300)
                    b=random.randint(-300, 300)
                    yus(a,b)
                s.update()
            yy.clear()
        xh+=5
        yh-=5
        xh2+=5
        yh2-=5
        xh3+=5
        yh3-=5
        xh4+=5
        yh4-=5
        xh5+=5
        yh5-=5
        time.sleep(0.0000000001)
        f.clear()
        s.update() 
    time.sleep(2)
    yu.setheading(0)

    def yue():
        yu.pencolor("#565B02")
        
        yu.up()
        yu.goto(90,230)
        yu.down()
        yu.begin_fill()
        yu.circle(-65, 360)
        yu.fillcolor("#787305")
        yu.end_fill()

    yue()
    def shu2(p,q,o,w):    
        for i in range(1):
        
            u.pencolor("#76475F")
            x = random.randint(p, q)
            y = random.randint(o, w+15)
            if p<=x<=p+20 and o<=y<=o+15:
                continue
            elif q-20<=x<=q and o<=y<=o+15:
                continue
            elif p<=x<=p+20 and w-15<=y<=w:
                continue
            elif q-20<=x<=q and w-15<=y<=w:
                continue
            
            elif p<=x<=p+40 and w<=y<=w+15:
                continue
            elif q-40<=x<=q and w<=y<=w+15:
                continue
            u.up()
            u.goto(x,y)
            u.down()
            u.pensize(2)
            u.right(30)
            u.forward(7)
            u.right(150)
            u.forward(7)
            u.right(random.randint(30, 150))
            s.update()
    a=15
    b=170

    bl.pencolor("#100F0F")
    bl.pensize("150")
    for i in range(180):
        a -= 1
        bl.up()
        bl.goto(a,b)
        bl.down()
        bl.clear()
        bl.forward(50)
        s.update()
        u.up()
        u.goto(-90,-70)
        u.down()
        shu2(-60-90,60-90,40-70,135-70)
    t.setheading(0)
    for i in range(200):
        u.up()
        u.goto(-90,-70)
        u.down()
        shu2(-60-90,60-90,40-70,135-70)
    for i in range(7):
        if 0<=i<=3:
            t.pensize(5)
            t.pencolor("#555554")
            t.up()
            t.goto(-100-i*18,-85-i*10)
            t.down()
            t.forward(10+i*25)
        if 4<=i<7:
            t.setheading(0)
            t.up()
            t.goto(-200+i*10,-85-i*10)
            t.down()
            t.forward(185-i*25)

    t.up()
    t.goto(-310,225)
    t.down()
    t.pencolor("white")
    t.write("微",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-310,165)
    t.down()
    t.pencolor("white")
    t.write("吟",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-310,105)
    t.down()
    t.pencolor("white")
    t.write("海",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-310,45)
    t.down()
    t.pencolor("white")
    t.write("月",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-310,-25)
    t.down()
    t.pencolor("white")
    t.write("生",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-310,-85)
    t.down()
    t.pencolor("white")
    t.write("岩",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-310,-145)
    t.down()
    t.pencolor("white")
    t.write("桂",font=('华文行楷',25))
    time.sleep(1)

    t.up()
    t.goto(-360,185)
    t.down()
    t.pencolor("white")
    t.write("长",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-360,125)
    t.down()
    t.pencolor("white")
    t.write("笑",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-360,65)
    t.down()
    t.pencolor("white")
    t.write("无",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-360,5)
    t.down()
    t.pencolor("white")
    t.write("风",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-360,-55)
    t.down()
    t.pencolor("white")
    t.write("起",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-360,-115)
    t.down()
    t.pencolor("white")
    t.write("涧",font=('华文行楷',25))
    time.sleep(0.4)
    t.up()
    t.goto(-360,-175)
    t.down()
    t.pencolor("white")
    t.write("松",font=('华文行楷',25))
    time.sleep(0.4)

q.onclick(peng)
turtle.done()
