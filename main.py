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