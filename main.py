import turtle
from turtle import *
import tkinter
import random

brik_color = ["green", "red", 'yellow', 'blue', "orange", 'white', 'royalblue', 'pink', 'salmon']




def move_paddle_left():
    x = paddle.xcor()
    paddle.setx(x + 20)


def move_paddle_right():
    x = paddle.xcor()
    paddle.setx(x - 20)


def main():
    for row in range(1):
        for column in range(2):
            cube = turtle.Turtle()
            cube.speed(0)
            cube.shape('square')
            cube.color(random.choice(brik_color))
            cube.penup()
            cube.goto(-290 + column * 22, 290 - row * 22)
            for _ in range(4):  # Draw each cell
                cube.forward(30)
                cube.right(90)
            cube.pendown()

    while True:
        window.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # Check for wall collisions
        if ball.xcor() > 290 or ball.xcor() < -290:
            ball.dx *= -1

        if ball.ycor() > 290:
            ball.dy *= -1

            # Paddle and ball collision
        if ball.ycor() < -240 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
                ball.dy *= -1

            # Brick and ball collision
        for brick in cube:
            if brick.distance(ball) < 20:
                    brick.goto(1000, 1000)  # Move brick out of sight
                    ball.dy *= -1

            # Check for game over
            if ball.ycor() < -290:
                ball.goto(0, 0)
                ball.dy *= -1
                # Reset bricks
                for brick in cube:
                    brick.goto(-240, 250 - cube.index(brick) * 25)


window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.listen()
window.onkeypress(move_paddle_left, "Right")
window.onkeypress(move_paddle_right, "Left")
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 3.95
ball.dy = -3.95
paddle = turtle.Turtle()
paddle.penup()
paddle.shape('square')
paddle.color('white')
paddle.penup()
paddle.goto(0, -260)
paddle.shapesize(stretch_wid=1, stretch_len=3)
window.mainloop()
if __name__ == "__main__":
    main()
