#Space Invaders
import turtle
import os
import math
import random
import winsound


#Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
#Draw a Border for the game(centered)
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("blue")
border_pen.penup()
border_pen.setposition(-250,-250)
border_pen.down()
border_pen.pensize(5)
for side in range(4):
    border_pen.fd(500)
    border_pen.lt(90)
border_pen.hideturtle()

#Scoreboard
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-240, 230)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = 'left', font = ("Comic Sans", 10, "normal"))
score_pen.hideturtle()

#Create the player Turtle
player = turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -200)
player.setheading(90)

playerspeed = 20

#Player movements
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -240:
        x = -240
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 240:
        x = 240
    player.setx(x)

def fire_bullet():
    #declare bulletstate as global
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
    #Move bullet just above Player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x,y)
        bullet.showturtle()
        winsound.PlaySound("laser.wav", winsound.SND_FILENAME)
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 30:
        return True
    else:
        return False


#Choose number of enemies
number_of_enemies = 5
#Create empty list of enemies
enemies = []
#Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

#Create the NPC enemies
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-180, 180)
    y = random.randint(120, 200)
    enemy.setposition(x, y)
    enemyspeed = 2

#Weapons mwhahaha
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 15

#Bulletstate, ready = ready to fire, fire = bullet is firing
bulletstate = "ready"

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main game processes
while True:
    for enemy in enemies:
        #Move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Boundary Borders
        if enemy.xcor() > 225:
            #Moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -225:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1

        #Check for collision
        if isCollision(bullet, enemy):
            #Reset Bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset enemy
            x = random.randint(-180, 180)
            y = random.randint(120, 200)
            enemy.setposition(x, y)
            winsound.PlaySound("explosion.wav", winsound.SND_FILENAME)
            #Update Scoreboard
            score += 100
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = 'left', font = ("Comic Sans", 10, "normal"))


        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            winsound.PlaySound("explosion.wav", winsound.SND_FILENAME)
            print("Game Over")
            break

    #Move bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Border checking for bulletspeed
    if bullet.ycor() >= 240:
        bullet.hideturtle()
        bulletstate = "ready"

delay = input("Press enter to exit.")
