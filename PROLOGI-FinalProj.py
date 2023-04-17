import random
import string
from tkinter import *
from tkinter import messagebox

class PasswordManager:
    def __init__(self, master):
        self.master = master
        master.title("PCGM: Password Creator, Generator, and Manager")
        self.master.geometry("350x400")
        self.master.config(bg="pink")

        # Create labels and entry widgets for website/application, username/email/phone number and password
        self.label0 = Label(master, text="Website/Application:")
        self.label0.grid(row=0, sticky=E)
        self.entry0 = Entry(master)
        self.entry0.grid(row=0, column=1)
        self.label1 = Label(master, text="Username/Email/Phone number:")
        self.label1.grid(row=1, sticky=W)
        self.entry1 = Entry(master)
        self.entry1.grid(row=1, column=1)

        self.label2 = Label(master, text="Password:")
        self.label2.grid(row=2, sticky=E)
        self.entry2 = Entry(master, show="")
        self.entry2.grid(row=2, column=1)

        # Create button for checking password strength and generating a new password
        self.button1 = Button(master, text="Check Password Strength", command=self.check_password_strength,bg="yellow", fg="black")
        self.button1.grid(row=3, column=0, pady=10)

        self.label4 = Label(master, text="Password Length:")
        self.label4.grid(row=4, sticky=E)
        self.pass_len = Entry(master)
        self.pass_len.grid(row=4, column=1)

        self.button2 = Button(master, text="Generate New Password", command=self.generate_password, bg="green", fg="white")
        self.button2.grid(row=5, column=1, pady=10)

        # Create label for displaying password strength and feedback
        self.label3 = Label(master, text="")
        self.label3.grid(row=3, column = 1, columnspan=2)

        # Button to save login credentials and password to a text file
        self.button3 = Button(master, text="Save Credentials", command=self.save_credentials, bg="maroon", fg="white")
        self.button3.grid(row=7, column=0, pady=10)
        
        self.label5 = Label(master, text="Enter File Name and extension:")
        self.label5.grid(row=8, sticky=E)
        self.save = Entry(master)
        self.save.grid(row=8, column=1)

        # Create button for clearing the entry fields
        self.clear_button = Button(master, text="Clear", command=self.clear_fields, bg='red', fg='white')
        self.clear_button.grid(row=9, column=1, pady=10)

        # Create button for copying the password to the clipboard
        self.copy_button = Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="blue", fg="white")
        self.copy_button.grid(row=9, column=0, pady=10)

    def check_password_strength(self):
        password = self.entry2.get()
        if len(password) < 8:
            self.label3.configure(text="Weak password: too short")
        elif len(password) > 32:
            self.label3.configure(text="Weak password: too long")
        elif not any(char.isdigit() for char in password):
            self.label3.configure(text="Weak password: no digits")
        elif not any(char.isupper() for char in password):
            self.label3.configure(text="Weak password: no uppercase letters")
        elif not any(char.islower() for char in password):
            self.label3.configure(text="Weak password: no lowercase letters")
        elif not any(char in string.punctuation for char in password):
            self.label3.configure(text="Weak password: no special characters")
        else:
            self.label3.configure(text="Strong password!")
            
    #THE USER WILL CHOOSE THE PASSWORD LENGTH FROM 1-32
    def generate_password(self):
        try:
            upper = string.ascii_uppercase
            lower = string.ascii_lowercase
            numbers = string.digits
            symbols = string.punctuation
            all_chars = upper + lower + numbers + symbols
            password_length = int(self.pass_len.get())
            password = ''.join(random.sample(all_chars, password_length))
            self.entry2.delete(0, END)
            self.entry2.insert(0, password)
            self.label3.configure(text="Generated password: " + password)

            # Save the login credentials and password to a file
            try:
                name = self.save.get()
                with open(name, "a") as file:
                    file.write( self.entry0.get() + ", " + self.entry1.get() + ", " + password + "\n")

                messagebox.showinfo("New Password Generated", f"New password has been generated and saved to {name}")
            # Raise error if no file name is inputted
            except:
                messagebox.showinfo("Error!", "Error! No file name inputted.")

        # Raise error if no password length is inputted
        except:
            messagebox.showinfo("Error!", "Error! No password length inputted.")

    def clear_fields(self):
        self.entry0.delete(0, END)
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.pass_len.delete(0, END)
        self.save.delete(0, END)
        self.label3.configure(text="")

    def save_credentials(self):
        try:
            file_name =  self.save.get()
            with open(file_name, "a") as file:
                    file.write( self.entry0.get() + ", " + self.entry1.get() + ", " + self.entry2.get() + "\n")
                
            messagebox.showinfo("Credentials saved", f"Username and password saved to {file_name}")
        # Raise error if no file name is inputted
        except:
            messagebox.showinfo("Error!", "Error! No file name inputted.")

    def copy_to_clipboard(self):
        password = self.entry2.get()
        self.master.clipboard_clear()
        self.master.clipboard_append(password)
        self.master.update()
        messagebox.showinfo("Copy to Clipboard", "Password has been copied to the clipboard")

root = Tk()
my_gui = PasswordManager(root)
root.mainloop()