from tkinter import *
import string
import random
import pyperclip


class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.master.resizable(0, 0)
        self.master.title("Password Generator")
        self.master.config(bg="white")

        # Password Length Label
        self.length_label = Label(self.master, text='PASSWORD LENGTH', font='arial 10 bold', bg="white")
        self.length_label.pack(pady=10)

        # Password Length Spinbox
        self.pass_len = IntVar()
        self.length_spinbox = Spinbox(self.master, from_=8, to_=32, textvariable=self.pass_len, width=15)
        self.length_spinbox.pack()

        # Generated Password Label
        self.pass_label = Label(self.master, text='GENERATED PASSWORD', font='arial 10 bold', bg="white")
        self.pass_label.pack(pady=10)

        # Generated Password Entry Field
        self.pass_str = StringVar()
        self.pass_entry = Entry(self.master, textvariable=self.pass_str, width=30)
        self.pass_entry.pack()

        # Generate Password Button
        self.generate_btn = Button(self.master, text="GENERATE PASSWORD", command=self.generate_password, bg="green", fg="white")
        self.generate_btn.pack(pady=10)

        # Copy Password Button
        self.copy_btn = Button(self.master, text='COPY TO CLIPBOARD', command=self.copy_password, bg="blue", fg="white")
        self.copy_btn.pack(pady=10)

        # Clear Button
        self.clear_btn = Button(self.master, text='CLEAR', command=self.clear_password, bg="red", fg="white")
        self.clear_btn.pack(pady=10)

    # Function to generate password
    def generate_password(self):
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        numbers = string.digits
        symbols = string.punctuation
        all_chars = upper + lower + numbers + symbols
        password = ''.join(random.sample(all_chars, self.pass_len.get()))
        self.pass_str.set(password)

    # Function to copy password to clipboard
    def copy_password(self):
        pyperclip.copy(self.pass_str.get())

    # Function to clear generated password field
    def clear_password(self):
        self.pass_str.set("")


if __name__ == "__main__":
    root = Tk()
    PasswordGenerator(root)
    root.mainloop()
