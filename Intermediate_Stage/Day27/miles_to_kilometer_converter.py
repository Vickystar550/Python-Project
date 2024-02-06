import tkinter as tk

# create the window:
window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=400)
window.config(pady=10, padx=10)

# LABELS:
first_label = tk.Label(text="Is equal to", font=("Arial", 20, "bold"))
first_label.grid(row=1, column=0)
first_label.config(padx=20, pady=25)

miles_label = tk.Label(text="Miles", font=("Arial", 20, "bold"))
miles_label.grid(row=0, column=2)
miles_label.config(padx=20, pady=20)

km_label = tk.Label(text="Km", font=("Arial", 20, "bold"))
km_label.grid(row=1, column=2)
km_label.config(padx=20, pady=25)

answer_label = tk.Label(text="0", font=("Arial", 20, "bold"))
answer_label.grid(row=1, column=1)
answer_label.config(padx=20, pady=25)

# ENTRY:
entry = tk.Entry(width=20)
entry.grid(row=0, column=1)


# BUTTON:
# --- Event Listener function:
def converter():
    """This function convert from miles to km"""
    km = float(entry.get()) * 1.60934
    answer_label.config(text=f"{km:.2f}")


calculate_button = tk.Button(text="Calculate", command=converter)
calculate_button.grid(row=2, column=1)
calculate_button.config(pady=10, padx=20)

window.mainloop()
