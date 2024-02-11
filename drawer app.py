import turtle
t = turtle.Turtle()
t.hideturtle()
import time
turtle.title("HAKAD TEKNO: Graphicer's Board 1A")

window = turtle.Screen()
window.bgcolor("black")

t.speed(0)
t.pensize(3)
t.penup()
t.goto(0, 0)
t.pencolor("cyan")
t.write("  HAKAD TEKNO \n  Company", align="center", font=("Arial", 24, "bold"))

time.sleep(5)  

t.clear()  
turtle.listen()
t = turtle.Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "pink", "brown", "gray", "cyan", "magenta", "indigo", "white", "lightgray",  "gold", "silver", "violet", "turquoise", "lime", "bisque"]
colors2 = ["mediumred","mediumorange","mediumyellow","mediumgreen","mediumblue","mediumpink","mediumbrown","gray","mediumcyan","purple","mediuminigo","lightwhite","meiumlightgray","bronz","mediumviolet","mediumturqoise","mediumlime","mediumbisque"]
colors3 = ["darkred","darkorange","darkyellow","darkgreen","darkblue","darkpink","darkbrown","darkgray","darkcyan","darkmagenta","darkindigo","darkwhite","darkgray","darkviolet","darkturqoise","darklime","darkbisque","black","darkblack"]
colors4 = ["red", "orange", "yellow", "green", "blue", "pink", "brown", "gray", "cyan", "magenta", "indigo", "white", "lightgray",  "gold", "silver", "violet", "turquoise", "lime", "bisque","mediumred","mediumorange","mediumyellow","mediumgreen","mediumblue","mediumpink","mediumbrown","gray","mediumcyan","purple","mediuminigo","lightwhite","meiumlightgray","bronz","mediumviolet","mediumturqoise","mediumlime","mediumbisque","darkred","darkorange","darkyellow","darkgreen","darkblue","darkpink","darkbrown","darkgray","darkcyan","darkmagenta","darkindigo","darkwhite","darkgray","darkviolet","darkturqoise","darklime","darkbisque","black","darkblack"]
current_color = 0
current_color2 = 0
current_color3 = 0
drawing = True

def change_color():
    global current_color
    current_color = (current_color + 1) % len(colors)
    t.pencolor(colors[current_color])

def draw(x, y):
    if drawing:
        t.pendown()
        t.goto(x, y)

def clear():
    t.clear()

def undo():
    t.undo()

def increase_thickness():
    t.width(t.width() + 1)  

def decrease_thickness():
    t.width(max(1, t.width() - 1))  

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def erase():
    t.penup()
    t.goto(t.pos())
    t.pendown()
    t.clear()

def toggle_drawing():
    global drawing
    drawing = not drawing
    if drawing:
        t.pendown()
    else:
        t.penup()

window = turtle.Screen()
window.bgcolor("white")

t.speed(0)
t.pensize(3)

window.onclick(draw)
window.onkeypress(change_color, "space")
window.onkeypress(clear, "c")
window.onkeypress(undo, "b")
window.onkeypress(move_forward, "w")
window.onkeypress(move_backward, "s")
window.onkeypress(turn_left, "d")
window.onkeypress(turn_right, "a")
window.onkeypress(increase_thickness, "k")  
window.onkeypress(decrease_thickness, "i")  

turtle.listen()
turtle.mainloop()