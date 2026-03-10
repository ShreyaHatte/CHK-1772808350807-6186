from cipher import encode_message, decode_message


def encode_action(message_entry, key_entry, result_label):
    message = message_entry.get()
    key = key_entry.get()

    if not key.isdigit():
        result_label.config(text="Key must be a number")
        return

    key = int(key)
    result = encode_message(message, key)
    result_label.config(text="Encoded: " + result)


def decode_action(message_entry, key_entry, result_label):
    message = message_entry.get()
    key = key_entry.get()

    if not key.isdigit():
        result_label.config(text="Key must be a number")
        return

    key = int(key)
    result = decode_message(message, key)
    result_label.config(text="Decoded: " + result)