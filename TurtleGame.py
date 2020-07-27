from turtle import Turtle
from random import randint

player1 = Turtle()
player1.color('purple')
player1.shape('turtle')

player1.penup()
player1.goto(-160,100)
player1.pendown()

player2 = Turtle()
player3 = Turtle()
player4 = Turtle()

player2.color('green')
player2.shape('turtle')
player2.penup()
player2.goto(-160,70)
player2.pendown()

player3.color('yellow')
player3.shape('turtle')
player3.penup()
player3.goto(-160,40)
player3.pendown()

player4.color('brown')
player4.shape('turtle')
player4.penup()
player4.goto(-160,10)
player4.pendown()

for movement in range(100):
  player1.forward(randint(1,5))
  player2.forward(randint(1,5))
  player3.forward(randint(1,5))
  player4.forward(randint(1,5))
