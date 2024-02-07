import tkinter as tk
import pandas
import random
from pandas.errors import EmptyDataError

# ------CONSTANT VARIABLES ------------------------
BACKGROUND_COLOR = "#B1DDC6"
FIRST_LANG = "French"
TRANSLATE_LANG = "English"
ORIGINAL_CSV = "data/french_words.csv"
SAVED_CSV = "data/words_to_learn.csv"
MILLI_SEC = 3000  # that is 1000 milli-secs


# ------------- Other variables ------------------
data = {}
current_card = {}

# ------------- READ DATA FROM FILES ---------------------
try:
    df = pandas.read_csv(SAVED_CSV)
except (FileNotFoundError, EmptyDataError):
    df = pandas.read_csv(ORIGINAL_CSV)
    data = df.to_dict(orient='records')
else:
    data = df.to_dict(orient="records")


# ----------- WORDS GENERATING FUNCTIONS ------------------
def next_card():
    """Generate a random word in the unknown language and show its english's meaning after every 3 minutes"""
    global timer
    window.after_cancel(timer)

    global current_card
    try:
        current_card = random.choice(data)
    except IndexError:
        # if IndexError, perform this tasks
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(card_title, text="END", fill="RED")
        canvas.itemconfig(card_word, text=f"No Words", fill="green")
    else:
        # else, perform this:
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(card_title, text=FIRST_LANG, fill="black")
        canvas.itemconfig(card_word, text=f"{current_card.get(FIRST_LANG)}", fill="black")
        # set a timer function to call the flip_card method after every 3 minutes
        timer = window.after(MILLI_SEC, flip_card)


def known_word():
    """Saves the unknown set of word-translation to a csv file
        """
    try:
        # remove the known word from the data list of words.
        data.remove(current_card)
    except ValueError:
        # print this to the canvas is there's a ValueError
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(card_title, text="Known All", fill="green")
        canvas.itemconfig(card_word, text=f"END", fill="green")
    else:
        # Perform this task is everything goes well:
        # create a new dataframe of unknown words, and save it to a csv file.
        new_df = pandas.DataFrame(data)
        new_df.to_csv("data/words_to_learn.csv", index=False)
        # call next_card function.
        next_card()


def flip_card():
    """Flip to show the correct English translation"""
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text=TRANSLATE_LANG, fill="white")
    canvas.itemconfig(card_word, text=f"{current_card.get(TRANSLATE_LANG)}", fill="white")


# ------------------------------- UI SETUP --------------------------#


# creating window/screen
window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(MILLI_SEC, flip_card)

# creating image objects to be used:
front_image = tk.PhotoImage(file="./images/card_front.png")
back_image = tk.PhotoImage(file="./images/card_back.png")
right_button_image = tk.PhotoImage(file="./images/right.png")
wrong_button_image = tk.PhotoImage(file="./images/wrong.png")

# creating the 1st canvas object:
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 268, image=front_image)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

# BUTTONS:
right_button = tk.Button(image=right_button_image, highlightthickness=0, command=known_word)
right_button.grid(row=2, column=2)

wrong_button = tk.Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=2, column=1)

# calling next_card function to initialize the canvas screen with starting values
next_card()

window.mainloop()
