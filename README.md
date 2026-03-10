
# CHK-1772808350807-6186

🔐 Secret Message Translator

A Python-based Secret Message Encoding and Decoding application that allows users to securely translate messages using a numeric key. The project uses a simple encryption technique similar to the Caesar Cipher to convert readable text into an encoded secret message.

This tool is designed for two people who want to communicate over a public chat while keeping their messages private.

📌 Problem Statement

Two people want to send a secret message across a public chat, but they do not want anyone else to understand the message.

They need a translation station where they can:

Enter a message

Provide a secret numeric key

Convert the message into an encoded form

Decode the message using the same key

🎯 Project Objectives

To create a simple encryption and decryption system

To allow secure communication using a secret key

To build a user-friendly GUI application using Python

To store message history using a database

⚙️ Technologies Used

Python

Tkinter (GUI)

SQLite Database

Git & GitHub

🧠 How It Works

The application uses a character shifting encryption algorithm.

1. User enters a message.

2. User selects a numeric key.

3. Each letter in the message shifts forward in the alphabet based on the key.

4. The encoded message is generated.

5. The same key can be used to decode the message back to its original form.

Example:

Original Message  
"HELLO"

Key: 3

Encoded Message  
"KHOOR"
