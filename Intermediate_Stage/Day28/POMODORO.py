import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """Reset the timing mechanism"""
    window.after_cancel(timer)  # cancels the timer effect
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, pady=5, padx=5, font=(FONT_NAME, 50, "bold"))
    canvas.itemconfig(timer_text, text="00:00")     # reconfigure the canvas display of time
    check_label.config(text="", fg=YELLOW)
    global reps
    reps = 0    # reset the reps to zero



# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """This function call the count_down function based on the specific reps"""
    global reps
    reps += 1       # increasing the reps each call of this function

    # converting each time variable to sec
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK", width=20, bg=YELLOW, fg=PINK, pady=5, padx=5, font=(FONT_NAME, 50, "bold"))
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK", width=20, bg=YELLOW, fg=RED, pady=5, padx=5, font=(FONT_NAME, 50, "bold"))
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", bg=YELLOW, fg=GREEN, pady=5, padx=5, font=(FONT_NAME, 50, "bold"))



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """This function serves as the time counter.
        Given an argument, it breaks it into the equivalent min and sec, and then counts it down"""

    # dividing the argument into its equivalent in minutes and seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # checks if the count_sec variable is less than 10
    if count_sec < 10:
        # Using dynamic type feature of python, change the count_sec to an string
        count_sec = f"0{count_sec}"

    # change the display on the canvas to read the counting time in the format of the text argument
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # call the window's after() function to repeat the count_down function every 1000sec (actual time)
        # as far as count > 0
        # pass the function argument of count - 1 to window's .after() method
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # if count is <= 0, call the start_timer function again
        start_timer()

        # adding a check emoji equivalent in count after each successfully session.
        emoji = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            emoji = "✔"
        check_label.config(text=emoji, fg=RED)


# ---------------------------- UI SETUP ------------------------------- #
# creating the window/screen:
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# creating the image object to be used:
tomato_image = tk.PhotoImage(file="tomato.png")

# creating the canvas object, adding image and text:
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


# LABELS:-----------------------

# creating the timer label
timer_label = tk.Label(width=5, text="Timer")
timer_label.config(bg=YELLOW, fg=GREEN, pady=5, padx=5, font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=1, column=2)

# creating the check label
check_label = tk.Label()
check_label.config(bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_label.grid(row=3, column=2)


# BUTTON:-----------------------

# creating the start button
start_button = tk.Button(text="start", command=start_timer)
start_button.config(font=(FONT_NAME, 20, "bold"))
start_button.grid(row=3, column=1)

# creating the reset button
reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.config(fg=YELLOW, font=(FONT_NAME, 20, "bold"))
reset_button.grid(row=3, column=3)

# maintain the game operation
window.mainloop()

