<<<<<<< HEAD
import tkinter as tk
from ui_action import encode_action, decode_action
from database import create_db
from database import get_messages
from tkinter import ttk

create_db()


def show_history():

    history_window = tk.Toplevel(window)
    history_window.title("Message History")
    history_window.geometry("700x400")

    columns = ("ID", "Message", "Result", "Key", "Action", "Time")

    tree = ttk.Treeview(history_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    data = get_messages()

    for row in data:
        tree.insert("", tk.END, values=row)

    tree.pack(fill="both", expand=True)
    
window = tk.Tk()
window.title("Secret Message Translation Station")
window.geometry("500x350")
window.configure(bg="#1e1e2f")

title = tk.Label(
    window,
    text="Secret Message Translator",
    font=("Helvetica", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=15)

frame = tk.Frame(window, bg="#1e1e2f")
frame.pack()

message_label = tk.Label(
    frame,
    text="Enter Message",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
message_label.grid(row=0, column=0, pady=5)

message_entry = tk.Entry(
    frame,
    width=35,
    font=("Arial", 11),
    bd=2,
    relief="groove"
)
message_entry.grid(row=0, column=1, pady=5)

key_label = tk.Label(
    frame,
    text="Enter Secret Key",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
key_label.grid(row=1, column=0, pady=5)

key_entry = tk.Entry(
    frame,
    width=20,
    font=("Arial", 11),
    bd=2,
    relief="groove"
)
key_entry.grid(row=1, column=1, pady=5)

encode_button = tk.Button(
    window,
    text="Encode Message",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=lambda: encode_action(message_entry, key_entry, result_label)
)
encode_button.pack(pady=10)

decode_button = tk.Button(
    window,
    text="Decode Message",
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    width=20,
    command=lambda: decode_action(message_entry, key_entry, result_label)
)
decode_button.pack(pady=5)

result_label = tk.Label(
    window,
    text="Result will appear here",
    font=("Arial", 13),
    bg="#2c2c3c",
    fg="white",
    width=40,
    height=2
)
result_label.pack(pady=20)

history_button = tk.Button(
    window,
    text="View Message History",
    bg="#9c27b0",
    fg="white",
    command=show_history
)

history_button.pack(pady=5)



window.mainloop()

=======
import tkinter as tk
from ui_action import encode_action, decode_action


window = tk.Tk()
window.title("Secret Message Translation Station")
window.geometry("500x350")


title = tk.Label(window, text="Secret Message Translator", font=("Arial", 16))
title.pack(pady=10)


message_label = tk.Label(window, text="Enter Message")
message_label.pack()

message_entry = tk.Entry(window, width=40)
message_entry.pack(pady=5)


key_label = tk.Label(window, text="Enter Secret Key")
key_label.pack()

key_entry = tk.Entry(window, width=20)
key_entry.pack(pady=5)


encode_button = tk.Button(
    window,
    text="Encode",
    bg="lightblue",
    command=lambda: encode_action(message_entry, key_entry, result_label)
)
encode_button.pack(pady=5)


decode_button = tk.Button(
    window,
    text="Decode",
    bg="lightgreen",
    command=lambda: decode_action(message_entry, key_entry, result_label)
)
decode_button.pack(pady=5)


result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)


window.mainloop()
>>>>>>> e21005cafe1d41569c322ec7cfc8baf403e523ac
