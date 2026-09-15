import tkinter as tk
import math
import random

WIDTH, HEIGHT = 900, 600

root = tk.Tk()
root.title("🕷️ Spider Love")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg="#080812")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#080812",
    highlightthickness=0
)
canvas.pack()

for _ in range(90):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    r = random.choice([1, 1, 2])
    canvas.create_oval(
        x-r, y-r, x+r, y+r,
        fill="#ffffff",
        outline=""
    )

spider_x = 120
spider_y = 350
dx = 3
shooting = False
web_length = 0
web_max = 380

def draw_spider(x, y):
    canvas.delete("spider")

    canvas.create_oval(
        x-28, y-35, x+28, y+35,
        fill="#17171f",
        outline="#ff1744",
        width=3,
        tags="spider"
    )

    canvas.create_oval(
        x-25, y-55, x+25, y-15,
        fill="#20202b",
        outline="#ff1744",
        width=2,
        tags="spider"
    )

    canvas.create_oval(
        x-16, y-45, x-7, y-36,
        fill="#ff3154",
        outline="",
        tags="spider"
    )

    canvas.create_oval(
        x+7, y-45, x+16, y-36,
        fill="#ff3154",
        outline="",
        tags="spider"
    )

    for side in [-1, 1]:
        for i in range(4):
            yy = y - 25 + i * 17
            canvas.create_line(
                x + side*18, yy,
                x + side*55, yy - 18,
                x + side*78, yy + 4,
                fill="#ff1744",
                width=4,
                smooth=True,
                tags="spider"
            )

    canvas.create_text(
        x, y+5,
        text="♥",
        fill="#ff1744",
        font=("Arial", 20, "bold"),
        tags="spider"
    )

def draw_web(x, y, length):
    canvas.delete("web")

    end_x = x + length
    end_y = y - 40

    canvas.create_line(
        x, y-35,
        end_x, end_y,
        fill="#eeeeff",
        width=2,
        tags="web"
    )

    for i in range(1, 6):
        t = i / 6
        cx = x + length * t
        cy = y - 35 - 5 * t

        canvas.create_oval(
            cx-4, cy-4,
            cx+4, cy+4,
            outline="#ffffff",
            width=1,
            tags="web"
        )

    for radius in [25, 50, 80, 110]:
        if radius < length:
            canvas.create_arc(
                end_x-radius,
                end_y-radius,
                end_x+radius,
                end_y+radius,
                start=190,
                extent=160,
                outline="#ddddff",
                width=1,
                tags="web"
            )

    canvas.create_text(
        end_x,
        end_y-55,
        text="LOVE U MARJOLA ❤️",
        fill="#ff4d6d",
        font=("Arial", 25, "bold"),
        tags="web"
    )

def animate():
    global spider_x, spider_y, dx, shooting, web_length

    spider_x += dx

    if spider_x > WIDTH - 100:
        dx = -3

    if spider_x < 100:
        dx = 3

    spider_y = 350 + math.sin(spider_x / 45) * 45

    draw_spider(spider_x, spider_y)

    if not shooting and random.random() < 0.008:
        shooting = True
        web_length = 0

    if shooting:
        web_length += 12

        if web_length >= web_max:
            web_length = web_max

        draw_web(spider_x, spider_y, web_length)

        if web_length >= web_max:
            root.after(1200, stop_web)

    root.after(30, animate)

def stop_web():
    global shooting
    shooting = False
    canvas.delete("web")

canvas.create_text(
    WIDTH//2,
    55,
    text="🕷️ SPIDER'S SECRET MESSAGE 🕷️",
    fill="#ff1744",
    font=("Arial", 27, "bold")
)

canvas.create_text(
    WIDTH//2,
    HEIGHT-35,
    text="Waiting for Marjola... ❤️",
    fill="#777788",
    font=("Arial", 13)
)

animate()

root.mainloop()
