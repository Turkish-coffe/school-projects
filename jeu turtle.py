import turtle
import random

#screen setup
wn = turtle.Screen()
wn.title("squares and circles")
wn.bgcolor("black")
wn.setup(width=800,height=800)
wn.tracer(0)

scoreplayer1 = 0
scoreplayer2 = 0

#add player1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.penup()
player1.goto(-120,-290)
player1.direction = "stop"

#add player2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("yellow")
player2.penup()
player2.goto(120,-290)
player2.direction = "stop"

#create a list of uchiha:
uchiha = [] 

#add sasuke
for w in range(10):
    sasuke = turtle.Turtle()
    sasuke.speed(0)
    sasuke.shape("circle")
    sasuke.color("blue")
    sasuke.penup()
    sasuke.goto(0,290)
    sasuke.speed = random.randint(1,3)
    uchiha.append(sasuke)

#create a list of uzumaki:
uzumaki = [] 

#add uzumaki
for w in range(10):
    naruto = turtle.Turtle()
    naruto.speed(0)
    naruto.shape("circle")
    naruto.color("red")
    naruto.penup()
    naruto.goto(0,290)
    naruto.speed = random.randint(1,3)
    uzumaki.append(naruto)

#make the pen player1
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,260)
font = ("Courier", 24, "normal")
pen.write("score:{}".format(scoreplayer1),align="right",font=font)


#make the pen player2
pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("yellow")
pen2.penup()
pen2.goto(0,260)
font = ("Courier", 24, "normal")
pen2.write("score:{}".format(scoreplayer2),align = "left",font=font)

#fonctions:
def go_left():
    player1.direction = "left"


def go_right():
    player1.direction = "right"
    
    
def go_left2():
    player2.direction = "left"
    

def go_right2():
    player2.direction = "right"
    
#Keyboard binds:
wn.listen()
wn.onkeypress(go_left,"q")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"Q")
wn.onkeypress(go_left,"A")
wn.onkeypress(go_right,"D")
wn.onkeypress(go_left2,"Left")
wn.onkeypress(go_right2,"Right")


#Main Game Loop
while True:
    
    #update screen:
    wn.update()
    
    #move the player1:
    if player1.direction == "left":
        x = player1.xcor()
        x -= 3
        player1.setx(x)
        if player1.xcor() < -400:
            go_right()
    
    if player1.direction == "right":
        x = player1.xcor()
        x += 3
        player1.setx(x)
        if player1.xcor() > 400:
            go_left()
     #move the player2:
    if player2.direction == "left":
        x = player2.xcor()
        x -= 3
        player2.setx(x)
        if player2.xcor() < -400:
            go_right2()
    if player2.direction == "right":
        x = player2.xcor()
        x += 3
        player2.setx(x)   
        if player2.xcor() > 400:
            go_left2()
    #move the uchiha:
    for sasuke in uchiha:    
        y = sasuke.ycor()
        y -= sasuke.speed
        sasuke.sety(y)
        
        #check if off the screen:
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            sasuke.goto(x,y)
            
        #check for a collision with the player1:
        if sasuke.distance(player1) < 20 :
            x = random.randint(-380,380)
            y = random.randint(300,400)
            sasuke.goto(x,y)
            scoreplayer1 += 1
            pen.clear()
            pen.write("score:{}".format(scoreplayer1),align="right",font=font)
            
                
         #check for a collision with the player2:
        if sasuke.distance(player2) < 20 :
            x = random.randint(-380,380)
            y = random.randint(300,400)
            sasuke.goto(x,y)
            scoreplayer2 += 1
            pen2.clear()
            pen2.write("score:{}".format(scoreplayer2),align = "left",font=font)
            
    #move the uzumaki:
    for naruto in uzumaki:    
        y=naruto.ycor()
        y -= naruto.speed
        naruto.sety(y)
        
        #check if off the screen:
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            naruto.goto(x,y)
            
        #check for a collision with the player1:
        if naruto.distance(player1) < 20 :
            x = random.randint(-380,380)
            y = random.randint(300,400)
            naruto.goto(x,y)
            scoreplayer1 -= 3
            pen.clear()
            pen.write("score:{}".format(scoreplayer1),align="right",font=font)
            
         #check for a collision with the player2:
        if naruto.distance(player2) < 20 :
            x = random.randint(-380,380)
            y = random.randint(300,400)
            naruto.goto(x,y)
            scoreplayer2 -= 3
            pen2.clear()
            pen2.write("score:{}".format(scoreplayer2),align = "left",font=font)
            
    if scoreplayer1 >= 20:
            pen.clear()
            pen2.clear()
            pen.write("WHITE WON",align="right",font=font)
            break
    if scoreplayer2 >= 20:
            pen.clear()
            pen2.clear()
            pen2.write("YELLOW WON",align = "left",font=font)
            break
wn.mainloop()

      
              
              
        
    


