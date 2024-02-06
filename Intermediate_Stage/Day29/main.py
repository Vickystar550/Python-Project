import tkinter as tk
from tkinter import messagebox
import password_generator
import pyperclip

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generate password and copied it to clipboard"""
    # get the password from the password_generator.py file
    password = password_generator.password()

    # paste password to clipboard
    pyperclip.copy(password)

    # clear the entry if the user had already entered password....
    password_entry.delete(0, "end")

    # insert the newly generated password
    password_entry.insert(0, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def remove_entries():
    website_entry.delete(0, "end")
    email_username_entry.delete(0, "end")
    email_username_entry.insert(0, string="james@gamil.com")
    password_entry.delete(0, "end")


def save_details():
    """Saves the login details to a file"""
    # Get entries:
    e_entry = email_username_entry.get()
    w_entry = website_entry.get()
    p_entry = password_entry.get()

    # Validate Entries:
    # 1. check against empty entries
    if len(w_entry) == 0 or len(p_entry) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # 2. reaffirm the user's entries:
        answer = messagebox.askokcancel(title=w_entry,
                                        message=f"These are the details entered: "
                                                f"\n\nEmail: {e_entry} \nPassword: {p_entry} \nIs it"
                                                f" okay to save?")

        if answer:
            # save entries in a text file
            with open("data.txt", mode="a") as file:
                file.write(f"{w_entry} | {e_entry} | {p_entry}\n")
            remove_entries()


# ---------------------------- UI SETUP ------------------------------- #
# creating window/screen
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# creating thr image object to be used
password_image = tk.PhotoImage(file="logo.png")

# creating the canvas object:
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=1, column=2)

# LABELS:
# 1. create the website label widget:
website_label = tk.Label(text="Website")
website_label.config(fg=GREEN, pady=10, padx=10, font=(FONT_NAME, 20, "normal"))
website_label.grid(row=2, column=1)

# 2. create the email/username label widget:
email_username_label = tk.Label(text="Email/Username")
email_username_label.config(fg=GREEN, pady=10, padx=10, font=(FONT_NAME, 20, "normal"))
email_username_label.grid(row=3, column=1)

# 3. create the password label widget:
password_label = tk.Label(text="Password")
password_label.config(fg=GREEN, pady=10, padx=10, font=(FONT_NAME, 20, "normal"))
password_label.grid(row=4, column=1)

# ENTRIES:
# 1. create the website entry widget:
website_entry = tk.Entry(width=35)
website_entry.focus()
website_entry.grid(row=2, column=2, columnspan=2)

# 2. create the email/username entry widget:
email_username_entry = tk.Entry(width=35)
email_username_entry.insert(0, string="james@gamil.com")
email_username_entry.grid(row=3, column=2, columnspan=2)

# 3. create the password entry widget:
password_entry = tk.Entry(width=21)
password_entry.grid(row=4, column=2)

# BUTTONS:
# 1. create the generate password button widget:
generate_password_button = tk.Button(text="Generate Password", command=generate_password, fg=YELLOW)
generate_password_button.grid(row=4, column=3)

# 2. create the add button widget:
add_button = tk.Button(text="Add", width=36, command=save_details)
add_button.grid(row=5, column=2, columnspan=2)

# maintain the program execution
window.mainloop()
