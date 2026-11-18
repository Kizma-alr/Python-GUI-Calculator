import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("350x500")
window.resizable(False, False)
window.configure(bg="lavenderblush")

expression = ""

display = tk.Entry(
    window,
    font=("Arial", 24),
    bg="pink",
    fg="deeppink4",
    insertbackground="deeppink4",
    justify="right",
    bd=0
)

display.pack(
    fill="x",
    padx=15,
    pady=20,
    ipady=20
)

def validate_input(event):
    if event.char.isdigit() or event.keysym in (
        "BackSpace", "Delete", "Left", "Right"
    ):
        return None
    return "break"

def sync_expression(event):
    global expression
    expression = display.get()

display.bind("<Key>", validate_input)
display.bind("<KeyRelease>", sync_expression)

def button_click(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def calculate():
    global expression
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERROR")
        expression = ""

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

button_frame = tk.Frame(
    window,
    bg="lavenderblush"
)

button_frame.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=5
)


clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 18, "bold"),
    bg="hotpink3",
    fg="black",
    bd=0,
    command=clear
)

clear_button.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=4,
    pady=4
)

for row_index, row in enumerate(buttons, start=1):    
    for col_index, value in enumerate(row):
        if value == "=":
            command = calculate
            color = "hotpink3"
        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: button_click(v)
            color = "mediumvioletred"
        else:
            command = lambda v=value: button_click(v)
            color = "violet"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            bd=0,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )

for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

window.mainloop()