from tkinter import *
import math
from datetime import datetime
from word_bank import WordBank

#  ############## CONSTANTS and Predefined Variables ###########

# time initials
start_time = None
end_time = None
total_seconds_spent = 0

# control variables
started = False
already_started = False
is_pause = False

# get copyright year
copyright_year = datetime.now().year

# initial the current passage index, and the current story index
current_passage_index = 0
current_storyline_index = 0

# ##################### STORIES, messages and instruction #########################
word_bank = WordBank()

storylines = word_bank.get_dict_values(d=word_bank.encyclopedia_dict)

current_story = storylines[current_storyline_index]

current_passage = ''
# ###################### FUNCTIONS #######################

# ------------------- Text or Comprehensive Passage Functions --------------------


def get_passage(lt):
    """get a comprehensive passage from a list or collection"""
    global current_passage_index

    try:
        wd = lt[current_passage_index]
    except IndexError:
        current_passage_index = 0
        return lt[current_passage_index]
    else:
        return wd
    finally:
        current_passage_index += 1


def generate_text(collection: list):
    """display a comprehensive text on the display canvas"""
    global current_passage
    current_passage = get_passage(lt=collection)
    # send current passage to WordBank class
    word_bank.current_passage = current_passage

    display_canvas.itemconfig(display_text, text=f'{current_passage}')

    # empty the previous text input
    input_widget.delete("1.0", "end")


def next_story():
    """get the next story """
    global current_storyline_index, current_passage_index
    current_storyline_index += 1
    current_passage_index = 0

    try:
        new_storyline = storylines[current_storyline_index]
    except IndexError:
        current_storyline_index = 0
        return storylines[current_storyline_index]
    else:
        return new_storyline


def change_storyline():
    """change the current storyline"""
    global current_story
    current_story = next_story()
    generate_text(collection=current_story)


def guidelines():
    """display the instruction to the game"""
    display_canvas.itemconfig(display_text,
                              text='PROBABLY NOTHING 🙂😄😎',
                              font=('San Serif', 40, 'normal'))

    # disable the instruction btn after it has been clicked
    guidelines_button.config(state='disabled')


# --------------------- Other Functions ---------------

def update_total_seconds_spent():
    global total_seconds_spent
    total_seconds_spent += math.floor((end_time - start_time).total_seconds())


def _from_rgb(rgb):
    """translates a rgb tuple of int to a tkinter friendly color code

    :return:
    returns a hex color code"""
    return "#%02x%02x%02x" % rgb


# ------------------- Timing Mechanism ----------------------

def timer(sec):
    """ Act like a stopwatch.
    Also display the timing mechanism on the canvas"""
    timer_text = report_time(sec=sec, for_="timer display")

    canvas.itemconfig(timer_display, text=timer_text, )

    if sec >= 0:
        # keep the timing
        global time_func
        time_func = window.after(1000, timer, sec + 1)

    # change the canvas display text color after 10 minutes
    if sec >= 300:
        canvas.itemconfig(timer_display, fill='yellow')


#  ----------------- Report/Summary Functions ----------------

def report_time(sec, for_: str):
    """Processes and report elapse time"""
    hours = math.floor(sec / 3600)
    minutes = math.floor(sec / 60)
    actual_sec = math.floor(sec % 60)

    if for_ == "timer display":
        if actual_sec < 10:
            actual_sec = f'0{actual_sec}'

        if minutes < 10:
            minutes = f'0{minutes}'

        if hours < 10:
            hours = f'0{hours}'

        return f'{hours}:{minutes}:{actual_sec}'
    elif for_ == "stats":
        return f'{hours} hr, {minutes} min, {actual_sec} sec'


def display_stats():
    """display the game start at the end"""

    # get user typed text or input
    word_bank.typed_text = input_widget.get("1.0", "end").strip()
    # send total time to WordBank class
    word_bank.total_time_spent = total_seconds_spent

    # get a time report
    time_report = report_time(sec=total_seconds_spent, for_='stats')

    message = word_bank.summary_statistics(time_report=time_report)

    text_info_label.config(text='Test Summary ↓↓↓')
    display_canvas.itemconfig(display_text,
                              text=message,
                              justify='left')


# ----------------------- Buttons Functions ---------------------

def start():
    """Start timer"""
    global already_started, start_time

    display_canvas.itemconfig(display_text, font=('Courier', 20, 'normal'))

    # change the start button display
    start_button.config(text='Restart')

    # change this widget-displayed text
    text_info_label.config(text='Text to Type ↓↓↓')

    # generate new text for display_canvas widget
    generate_text(collection=current_story)

    # enable some tkinter widgets: (Stop Button, Pause Button, Input Text Widget, New Text Button)
    input_widget.config(state='normal')
    new_text_button.config(state='normal')
    pause_play_button.config(state='normal')
    stop_button.config(state='normal', fg='black', bg='red')
    change_storyline_button.config(state='normal')
    guidelines_button.config(state='disabled')

    # empty the previous text input
    input_widget.delete("1.0", "end")

    if already_started:
        # kill the time_func first
        window.after_cancel(time_func)
        # reconfigure the canvas display of time
        canvas.itemconfig(timer_display, text="00:00:00", fill='black')
        # reset timer
        timer(sec=0)
    else:
        # start the stopwatch
        timer(sec=0)

    # set a global start_time variable
    start_time = datetime.now()

    # set already_started to True
    already_started = True


def stop():
    """Stop timer"""
    global end_time, start_time, total_seconds_spent, started, \
        current_storyline_index, current_passage_index, already_started, is_pause, current_passage

    # get the end time variable
    end_time = datetime.now()

    # update time records
    update_total_seconds_spent()

    # stop the timer and reset canvas timer_display:
    window.after_cancel(time_func)

    # reconfigure the canvas display of time
    canvas.itemconfig(timer_display, text="00:00:00", fill='black')

    # display the game statistics
    display_stats()

    # change the start button display text
    start_button.config(text='Start')

    # disable some tkinter widgets: (Stop Button, Pause Button, Input Text Widget, New Text Button)
    input_widget.config(state='disabled')
    new_text_button.config(state='disabled')
    pause_play_button.config(state='disabled')
    stop_button.config(state='disabled', fg='white',
                       bg=_from_rgb((45, 45, 45)))
    change_storyline_button.config(state='disabled')
    guidelines_button.config(state='normal')

    # reset end_time, start_time, started, current_storyline_index, current_passage_index, etc
    total_seconds_spent = 0
    current_storyline_index = 0
    current_passage_index = 0
    start_time = None
    end_time = None
    started = False
    already_started = False
    is_pause = False
    current_passage = ''


def pause():
    """Acts like a Pause Button Function"""
    global end_time, is_pause

    # get the end time variable
    end_time = datetime.now()

    # update total seconds spent
    update_total_seconds_spent()

    # stop the tkinter window's timing function
    window.after_cancel(time_func)

    # disable some tkinter widgets: (Stop Button, Start Button,  Input Text Widget, New Text Button)
    input_widget.config(state="disabled")
    stop_button.config(state='disabled')
    start_button.config(state='disabled')
    new_text_button.config(state='disabled')
    change_storyline_button.config(state='disabled')
    guidelines_button.config(state='disabled')

    # change the button display to "Play"
    pause_play_button.config(text='Play')

    # reset is_pause to True
    is_pause = True


def play():
    """Act like a Play Button Function"""
    # get the estimate of the last total_seconds spent
    global start_time, is_pause

    # reset the START_TIME variable
    start_time = datetime.now()

    # restart the stopwatch
    timer(sec=total_seconds_spent)

    # enable some tkinter widgets: (Stop Button, Start Button,  Input Text Widget, New Text Button)
    input_widget.config(state='normal')
    stop_button.config(state='normal')
    start_button.config(state='normal')
    new_text_button.config(state='normal')
    change_storyline_button.config(state='normal')
    guidelines_button.config(state='disabled')

    # change button text to "Pause"
    pause_play_button.config(text='Pause')

    # reset is_pause to False
    is_pause = False


def pausing_function():
    """pause and play the game"""
    if is_pause:
        # activate play
        play()
    else:
        # activate pause
        pause()


# #################### UI SETUP ##############################
window = Tk()
window.title(f'© {copyright_year} Victor Nice')
window.minsize(width=1500, height=1000)
window.config(pady=50, padx=50,)


# ROW 0
welcome_label = Label(text="Welcome to our Typing Speed Test App",
                      font=('Serif', 30, 'bold'))
welcome_label.grid(row=0, column=0, columnspan=3)
welcome_label.config(padx=20, pady=20, fg='white', )

# ROW 1
change_storyline_button = Button(text='Change Storyline', highlightthickness=0,
                                 width=15, command=change_storyline)
change_storyline_button.config(padx=20, pady=10, font=('San Serif', 20, 'normal'),
                               fg='sea green', state='disabled')
change_storyline_button.grid(row=1, column=0)

text_info_label = Label(text='Text to Type ↓ ↓ ↓',
                        font=('San Serif', 20, 'normal'), )
text_info_label.grid(row=1, column=1, )
text_info_label.config(padx=20, pady=10, fg='grey')

guidelines_button = Button(text='Guidelines', highlightthickness=0,
                           width=15, command=guidelines)
guidelines_button.config(padx=20, pady=10, font=('San Serif', 20, 'normal'),
                         fg='yellow', state='normal')
guidelines_button.grid(row=1, column=2)

# ROW 2
display_canvas = Canvas(width=1330, height=450, highlightthickness=0)
display_canvas.grid(row=2, column=0, columnspan=3, padx=20, pady=10, )
display_canvas.config(bg='black', )
display_text = display_canvas.create_text((665, 225),
                                          text=f"{word_bank.start_message}",
                                          font=('Courier', 20, 'normal'),
                                          fill='white',
                                          justify='left',
                                          width=1200,)

# ROW 3
new_text_button = Button(text='New Text', highlightthickness=0, width=10,
                         command=lambda: generate_text(collection=current_story))
new_text_button.config(padx=20, pady=10, font=('San Serif', 20, 'normal'),
                       fg='sea green', state='disabled')
new_text_button.grid(row=3, column=0)

start_button = Button(text='Start', highlightthickness=0, command=start, width=5)
start_button.config(padx=20, pady=10, font=('San Serif', 20, 'normal'), fg='black', bg='green', )
start_button.grid(row=3, column=2)

type_info_label = Label(text='Type Here ↓ ↓ ↓', font=('San Serif', 20, 'normal'), )
type_info_label.grid(row=3, column=1)
type_info_label.config(padx=20, pady=20, fg='grey')

# ROW 4
input_widget = Text(height=5, highlightcolor='grey', insertwidth=5, )
input_widget.focus()
# ------------ prevent backspacing, copying, and pasting on the input widget ------------
input_widget.bind('<Control-v>', lambda _: 'break')
input_widget.bind('<Control-c>', lambda _: 'break')
input_widget.bind('<Insert>', lambda _: 'break')
# input_widget.bind('<BackSpace>', lambda _: 'break')  ---- # please let there be backspace
# --------------------------------------------------------------------------
input_widget.grid(row=4, column=0, columnspan=3)
input_widget.config(padx=20, pady=20,
                    font=('Courier', 20, 'normal'),
                    state='disabled',
                    wrap='word',
                    undo=True,
                    maxundo=20,
                    autoseparators=True,
                    exportselection=False)

# ROW 5

pause_play_button = Button(text='Pause', highlightthickness=0, command=pausing_function, width=10)
pause_play_button.config(padx=20, pady=10, font=('San Serif', 20, 'normal',),
                         fg='orange', state='disabled')
pause_play_button.grid(row=5, column=0)

canvas = Canvas(width=250, height=60, highlightthickness=0)
canvas.config(bg='grey')
timer_display = canvas.create_text((125, 30), text='00:00:00', font=('Ariel', 30, 'bold'))
canvas.grid(row=5, column=1, padx=20, pady=20)


stop_button = Button(text='Stop', highlightthickness=0, command=stop, width=5)
stop_button.config(padx=20, pady=10, font=('San Serif', 20, 'normal'), state='disabled',)
stop_button.grid(row=5, column=2)

# MAINTAIN LOOP
window.mainloop()
