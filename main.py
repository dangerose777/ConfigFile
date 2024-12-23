import tkinter as tk
from tkinter import ttk

# >>> FUNCTIONS <<<

def read_config():
    try:
        with open("config.txt", "r") as file:
            line = file.readlines()
            color = line[0].strip() if len(line) > 0 else ""
            checkbox_state = line[1].strip() if len(line) > 1 else "0"
            return color, checkbox_state
    except FileNotFoundError:
        return "", "0"

def write_config(color, checkbox_state):
    with open("config.txt", "w") as file:
        file.write(color + "\n")
        file.write(checkbox_state + "\n")

def buttonDark_click():
    _, checkbox_state = read_config()
    write_config("dark", checkbox_state)
    update_ui()

def buttonLight_click():
    _, checkbox_state = read_config()
    write_config("light", checkbox_state)
    update_ui()

def checkbox_toggle():
    color, _ = read_config()
    new_state = "1" if checkbox_var.get() else "0"
    write_config(color, new_state)
    update_ui()

def update_ui():
    color, checkbox_state = read_config()

    if color == "dark":
        window.configure(bg="black")
    elif color == "light":
        window.configure(bg="white")

    if checkbox_state == "1":
        label.config(text="Checked")
        checkbox_var.set(True)
    else:
        label.config(text="")
        checkbox_var.set(False)

window = tk.Tk()
window.title("Config File Test")
window.geometry("300x200")

red_button = tk.Button(window, text="Dark", bg="black", fg="white", command=buttonDark_click)
red_button.pack(pady=5)

blue_button = tk.Button(window, text="Light", bg="white", fg="black", command=buttonLight_click)
blue_button.pack(pady=5)

checkbox_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(window, text="Checkbox", variable=checkbox_var, command=checkbox_toggle)
checkbox.pack(pady=10)

label = tk.Label(window, text="", font=("Arial", 12))
label.pack(pady=5)

update_ui()
window.mainloop()