# EnigmaKey (Password Generator & Strength Checker)

## Programming Language:
Created using [Python](https://www.python.org/) with the following libraries:
- [tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI
- [random](https://docs.python.org/3/library/random.html) for password generation
- [string](https://docs.python.org/3/library/string.html) for checking strength
- [hashlib](https://docs.python.org/3/library/hashlib.html) for encrypting saved passwords

## Description:
- This program is a proof of concept of a password generator and strength checker in python
- First, it takes a username or an email
- Optionally, a password, for which it will test its strength
- Recommendations about the password will be printed
- It can also generate its own password according to a length entered by the user
- Generated passwords are encrypted and stored in an external file
- There is also an option to copy password to clipboard
