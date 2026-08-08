import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


root = tk.Tk()
root.title("Pomodoro Timer")
root.attributes("-fullscreen", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.bind(
    "<Escape>",
    lambda event: root.attributes("-fullscreen", False)
)




# font checking kasi parusa
available_fonts = tkfont.families()

print("\n================================")
print("PIXEL FONTS FOUND:")
print("================================")

pixel_fonts = []

for f in available_fonts:
    if "pixel" in f.lower() or "operator" in f.lower():
        pixel_fonts.append(f)
        print(f)


TIMER_FONT = None

for f in available_fonts:
    if f.lower() == "pixel operator":
        TIMER_FONT = f
        break

if TIMER_FONT is None:
    for f in available_fonts:
        if "pixel operator" in f.lower():
            TIMER_FONT = f
            break

if TIMER_FONT is None and pixel_fonts:
    TIMER_FONT = pixel_fonts[0]

if TIMER_FONT is None:
    TIMER_FONT = "Arial"
    print("WARNING: Pixel Operator was NOT found.")
    print("Timer will use Arial.")
else:
    print("USING TIMER FONT:", TIMER_FONT)

print("================================\n")



# yay opening screen
def show_opening_screen():

    global opening_background
    global opening_start_image
    global opening_info_image

    for widget in root.winfo_children():
        widget.destroy()


    background = Image.open("@arvyarl ewan ko na.jpg")

    background = background.resize(
        (screen_width, screen_height),
        Image.Resampling.LANCZOS
    )

    opening_background = ImageTk.PhotoImage(background)

    canvas = tk.Canvas(
        root,
        width=screen_width,
        height=screen_height,
        highlightthickness=0,
        bd=0
    )

    canvas.pack(
        fill="both",
        expand=True
    )

    # Background
    canvas.create_image(
        0,
        0,
        image=opening_background,
        anchor="nw"
    )

# opening screen: start button
    start_image = Image.open("start.png")

    # Large button
    # thumbnail keeps the original proportions
    start_image.thumbnail(
        (850, 780),
        Image.Resampling.NEAREST
    )

    opening_start_image = ImageTk.PhotoImage(start_image)

    start_button = canvas.create_image(
        screen_width // 2,
        screen_height - 170,
        image=opening_start_image,
        anchor="center"
    )

# opening screen: info button
    info_image = Image.open("info.png")

    info_image.thumbnail(
        (300, 205),
        Image.Resampling.NEAREST
    )

    opening_info_image = ImageTk.PhotoImage(info_image)

    info_button = canvas.create_image(
        screen_width - 75,
        screen_height - 75,
        image=opening_info_image,
        anchor="center"
    )

    canvas.tag_bind(
        start_button,
        "<Button-1>",
        lambda event: show_timer_screen()
    )

    canvas.tag_bind(
        info_button,
        "<Button-1>",
        lambda event: show_info()
    )

# opening screen: info button: inside
def show_info():

    info_window = tk.Toplevel(root)
    info_window.title("Pomodoro Info")

    # Make info window fullscreen
    info_window.attributes("-fullscreen", True)

    info_width = info_window.winfo_screenwidth()
    info_height = info_window.winfo_screenheight()

    info_bg = Image.open("info_bg.jpg")

    img_ratio = info_bg.width / info_bg.height
    screen_ratio = info_width / info_height

    if img_ratio > screen_ratio:
        new_height = info_height
        new_width = int(new_height * img_ratio)
    else:
        new_width = info_width
        new_height = int(new_width / img_ratio)

    info_bg = info_bg.resize(
        (new_width, new_height),
        Image.Resampling.LANCZOS
    )

    left = (new_width - info_width) // 2
    top = (new_height - info_height) // 2

    info_bg = info_bg.crop(
        (
            left,
            top,
            left + info_width,
            top + info_height
        )
    )

    info_background = ImageTk.PhotoImage(info_bg)


    info_canvas = tk.Canvas(
        info_window,
        width=info_width,
        height=info_height,
        highlightthickness=0,
        bd=0
    )

    info_canvas.pack(
        fill="both",
        expand=True
    )

    info_canvas.create_image(
        0,
        0,
        image=info_background,
        anchor="nw"
    )

    info_window.info_background = info_background

    info_canvas.create_text(
        info_width * 0.50,
        info_height * 0.35,
        text="POMODORO TIMER",
        fill="#7b3028",
        font=(TIMER_FONT, 55, "bold"),
        anchor="center"
    )

    info_canvas.create_text(
        info_width * 0.50,
        info_height * 0.415,
        text="25 MINUTES - WORK",
        fill="#7b3028",
        font=(TIMER_FONT, 30, "bold"),
        anchor="center"
    )

    info_canvas.create_text(
        info_width * 0.50,
        info_height * 0.48,
        text="5 MINUTES - SHORT BREAK",
        fill="#7b3028",
        font=(TIMER_FONT, 30, "bold"),
        anchor="center"
    )

    info_canvas.create_text(
        info_width * 0.50,
        info_height * 0.545,
        text="20 MINUTES - LONG BREAK",
        fill="#7b3028",
        font=(TIMER_FONT, 30, "bold"),
        anchor="center"
    )

    info_canvas.create_text(
        info_width * 0.50,
        info_height * 0.61,
        text="! LONG BREAK AFTER 4 WORK SESSIONS",
        fill="#7b3028",
        font=(TIMER_FONT, 25, "bold"),
        anchor="center"
    )

    info_window.bind(
        "<Escape>",
        lambda event: info_window.destroy()
    )

    info_window.focus_force()

# timer screen
def show_timer_screen():

    global timer_background
    global timer_start_image
    global timer_reset_image
    global timer_text
    global timer_canvas
    global timer

    if timer is not None:
        root.after_cancel(timer)
        timer = None

    for widget in root.winfo_children():
        widget.destroy()

    background = Image.open("timer_bg.jpg")

    background = background.resize(
        (screen_width, screen_height),
        Image.Resampling.LANCZOS
    )

    timer_background = ImageTk.PhotoImage(background)

    timer_canvas = tk.Canvas(
        root,
        width=screen_width,
        height=screen_height,
        highlightthickness=0,
        bd=0
    )

    timer_canvas.pack(
        fill="both",
        expand=True
    )

    # Background
    timer_canvas.create_image(
        0,
        0,
        image=timer_background,
        anchor="nw"
    )

# main purpose hanep na timer to
    timer_text = timer_canvas.create_text(
        screen_width * 0.50,
        screen_height * 0.43,

        text="25:00",

        fill="white",

        font=(
            TIMER_FONT,
            150
        ),

        anchor="center"
    )

# timer screen: start button
    start_image = Image.open(
        "Untitled - August 08, 2026 at 23.48.27.png"
    )

    start_image = start_image.resize(
        (180, 80),
        Image.Resampling.NEAREST
    )

    timer_start_image = ImageTk.PhotoImage(
        start_image
    )

    start_button = timer_canvas.create_image(
        screen_width * 0.42,
        screen_height * 0.68,
        image=timer_start_image,
        anchor="center"
    )

    timer_canvas.tag_bind(
        start_button,
        "<Button-1>",
        lambda event: start_timer()
    )

# timer screen: reset button
    reset_image = Image.open(
        "Untitled - August 08, 2026 at 23.48.49.png"
    )

    reset_image = reset_image.resize(
        (180, 80),
        Image.Resampling.NEAREST
    )

    timer_reset_image = ImageTk.PhotoImage(
        reset_image
    )

    reset_button = timer_canvas.create_image(
        screen_width * 0.58,
        screen_height * 0.68,
        image=timer_reset_image,
        anchor="center"
    )

    timer_canvas.tag_bind(
        reset_button,
        "<Button-1>",
        lambda event: reset_timer()
    )

# start timer
def start_timer():

    global reps
    global timer

    if timer is not None:
        return

    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:

        count_down(long_break_seconds)


    elif reps % 2 == 0:

        count_down(short_break_seconds)


    else:

        count_down(work_seconds)

# coubtdown
def count_down(count):

    global timer

    minutes = count // 60
    seconds = count % 60

    timer_canvas.itemconfig(
        timer_text,
        text=f"{minutes}:{seconds:02d}"
    )

    if count > 0:

        timer = root.after(
            1000,
            count_down,
            count - 1
        )

    else:

        timer = None

        # Automatically start next session
        start_timer()

# reset after countdown/session
def reset_timer():

    global timer
    global reps

    reps = 0

    if timer is not None:

        root.after_cancel(timer)

        timer = None


    timer_canvas.itemconfig(
        timer_text,
        text="25:00"
    )



show_opening_screen()

root.mainloop()