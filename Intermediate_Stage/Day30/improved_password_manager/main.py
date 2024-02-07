import tkinter as tk
from tkinter import messagebox
import password_generator
import pyperclip
import json

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

    # create a dictionary with that will serves as the database:
    new_data = {
        w_entry: {
            "email": e_entry,
            "password": p_entry
        }
    }

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
            try:
                # read stored json data in a json file, and update it with the new_data
                with open("data.json", mode="r") as json_file:
                    # reading old data
                    data = json.load(json_file)
            except FileNotFoundError:
                # create a new json file and store the new_data:
                with open("data.json", mode="w") as json_file:
                    json.dump(new_data, json_file, indent=4)
            else:
                # updating old data with new one
                data.update(new_data)

                # save next entry to the created json file:
                with open("data.json", mode="w") as new_file:
                    json.dump(data, new_file, indent=4)
            finally:
                # clear already typed entries for another entries
                remove_entries()

# ----------------------------SEARCH------------------------------------- #


def search_details():
    """Searches the store database and returns the user's email and password for each website"""
    # Get website entry:
    w_entry = website_entry.get()

    try:
        # read from the stored database
        with open("data.json", mode="r") as data_file:
            # saving the read file to a variable. note the variable type is <dict>
            data_dict = json.load(data_file)

    except FileNotFoundError:
        # if raise FileNotFoundError, display an error message box
        messagebox.showerror(title="No Database", message="No Data File Found")

    else:
        # try this out if error is not raise. N/B using if-else can also work, but i just want to explore
        try:
            # check if website is a data_dict key:
            w_dict = data_dict[w_entry]
        except KeyError:
            # display a error message box if website does not exist:
            messagebox.showerror(title="Error", message="No details for the website exists.")
            # clear the website entry:
            website_entry.delete(0, "end")
        else:
            # if website exist, display the required info
            messagebox.showinfo(title=f"{w_entry}", message=f"Email:\t{w_dict['email']}\t\n\n"
                                                            f"Password:\t{w_dict['password']}\t")
            
            # optional features: add password to clipboard:
            pyperclip.copy(w_dict['password'])


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
website_entry.grid(row=2, column=2)

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

# 3. adding the search button:
search_button = tk.Button(text="Search", width=10, fg=YELLOW, command=search_details)
search_button.grid(row=2, column=3)


# maintain the program execution
window.mainloop()
