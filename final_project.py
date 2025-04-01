import turtle as t

YouScore = 0
You2Score = 0

window = t.Screen()
window.title("Valeria Final Project Ping Pong")
window.setup(800, 600)
window.tracer(0)

paddle_1 = t.Turtle()
paddle_1.speed()
paddle_1.shape("circle")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto()

paddle_2 = t.Turtle()
paddle_2.speed()
paddle_2.shape("circle")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto()
