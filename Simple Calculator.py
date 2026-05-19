import tkinter as tk

# Main window
root = tk.Tk()
root.title("Beautiful Calculator")
root.geometry("450x500")
root.configure(bg="#1e1e2f")

# Data structure
history = []

# Functions
# ----------------------------
def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    result = num1 + num2

    result_label.config(text="Answer = " + str(result))

    history.append("Addition = " + str(result))


def subtract():
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    result = num1 - num2

    result_label.config(text="Answer = " + str(result))

    history.append("Subtraction = " + str(result))


def show_history():

    history_box.delete("1.0", tk.END)

    for item in history:
        history_box.insert(tk.END, item + "\n")


# Heading
heading = tk.Label(
    root,
    text="Simple Calculator",
    font=("Helvetica", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
heading.pack(pady=20)

# First Number
label1 = tk.Label(
    root,
    text="First Number",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
label1.pack()

entry1 = tk.Entry(
    root,
    font=("Arial", 14),
    width=20,
    bd=3,
    relief="groove",
    justify="center"
)
entry1.pack(pady=10)

# Second Number
label2 = tk.Label(
    root,
    text="Second Number",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
label2.pack()

entry2 = tk.Entry(
    root,
    font=("Arial", 14),
    width=20,
    bd=3,
    relief="groove",
    justify="center"
)
entry2.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=15)

# Add Button
add_button = tk.Button(
    button_frame,
    text="Add",
    command=add,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=10,
    relief="flat",
    cursor="hand2"
)
add_button.grid(row=0, column=0, padx=10)

# Subtract Button
subtract_button = tk.Button(
    button_frame,
    text="Subtract",
    command=subtract,
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    width=10,
    relief="flat",
    cursor="hand2"
)
subtract_button.grid(row=0, column=1, padx=10)

# History Button
history_button = tk.Button(
    root,
    text="Show History",
    command=show_history,
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    width=20,
    relief="flat",
    cursor="hand2"
)
history_button.pack(pady=10)

# Result Label
result_label = tk.Label(
    root,
    text="Answer = ",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="#FFD700"
)
result_label.pack(pady=15)

# History Box
history_box = tk.Text(
    root,
    height=10,
    width=35,
    font=("Consolas", 11),
    bd=3,
    relief="ridge",
    bg="#f5f5f5"
)
history_box.pack(pady=10)

# Run Window
root.mainloop()