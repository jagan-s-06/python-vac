import tkinter as tk

window = tk.Tk()
window.title("Bouncing Ball")

WIDTH = 600
HEIGHT = 400

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

ball = canvas.create_oval(10, 10, 60, 60, fill="red")

x_speed = 3
y_speed = 3


def move_ball():
    global x_speed, y_speed

    canvas.move(ball, x_speed, y_speed)

    position = canvas.coords(ball)

    # Bounce vertically
    if position[3] >= HEIGHT or position[1] <= 0:
        y_speed = -y_speed

    # Bounce horizontally
    if position[2] >= WIDTH or position[0] <= 0:
        x_speed = -x_speed

    # Repeat every 10 ms
    window.after(10, move_ball)


move_ball()

window.mainloop()
