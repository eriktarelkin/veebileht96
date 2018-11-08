import turtle
import time
import random

aeglustamine = 0.1
#ekraan
ekraan = turtle.Screen()
ekraan.title('KertjaErikSnaEik')
ekraan.bgcolor('purple')
ekraan.setup(width = 600, height = 600)
ekraan.tracer(0) # lülitab ekraani vaelja

#Pea
pea = turtle.Turtle()
pea.speed(0)
pea.shape('square')
pea.color('green')
pea.penup()
pea.goto(0,0)
pea.direction = 'peatu'

#SööK
söök = turtle.Turtle()
söök.speed(0)
söök.shape('circle')
söök.color('yellow')
söök.penup()
söök.goto(0,100)


lülid = []

#funktsioonid mängu jaoks
def mine_üles():
    pea.direction = 'üles'
    
def mine_alla():
    pea.direction = 'alla'
    
def mine_vasakule():
    pea.direction = 'vasakule'
    
def mine_paremale():
    pea.direction = 'paremale'
    
def liikumine():
    if pea.direction == 'üles':
        y = pea.ycor()
        pea.sety(y + 20)
        
    if pea.direction == 'alla':
        y = pea.ycor()
        pea.sety(y - 20)
        
    if pea.direction == 'vasakule':
        x = pea.xcor()
        pea.setx(x - 20)
        
    if pea.direction == 'paremale':
        x = pea.xcor()
        pea.setx(x + 20)
        
# Klaviatuuri(nuppude) kasutamine
ekraan.listen()
ekraan.onkeypress(mine_üles, 'w')
ekraan.onkeypress(mine_alla, 's')
ekraan.onkeypress(mine_vasakule, 'a')
ekraan.onkeypress(mine_paremale, 'd')

# Põhiline mänguosa
while True:
    ekraan.update()
    
    #Kokkupõrge ekraani äärega
    if pea.xcor()>290 or pea.xcor()<-290 or pea.ycor()>290 or pea.ycor()<-290:
        time.sleep(1)
        pea.goto(0, 0)
        pea.direction = 'peatu'
        
        
        #Peida lülid
        for uus_lüli in lülid:
            uus_lüli.goto(1000,1000)
        
        
        #Puhasta lülide list
        lülid.clear()
    
    # Kokkupuude söögiga
    if pea.distance(söök) < 20:
        #söök suvakasse kohta
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        söök.goto(x, y)
        
        #lüli juurde
        uus_lüli = turtle.Turtle()
        uus_lüli.speed(0)
        uus_lüli.shape('square')
        uus_lüli.color('black')
        uus_lüli.penup()
        lülid.append(uus_lüli)
        
    #Lülide liikumine
    for index in range(len(lülid)-1, 0, -1):
        x = lülid[index - 1].xcor()
        y = lülid[index - 1].ycor()
        lülid[index].goto(x, y)
    # Lüli nulli
    if len(lülid) > 0:
        x = pea.xcor()
        y = pea.ycor()
        lülid[0].goto(x,y)
        
    liikumine()
    
    #Endaga kokkupõrge
    for uus_lüli in lülid:
        if uus_lüli.distance(pea) < 20:
            time.sleep(1)
            pea.goto(0, 0)
            pea.direction = 'peatu'
            
            
    time.sleep(aeglustamine) # et näeks midagi :)))

ekraan.mainloop()
