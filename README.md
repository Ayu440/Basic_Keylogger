# Basic_Keylogger
It's a basic keylogger written in python for learning purposes
# Basic Keylogger using Pynput

## Introduction
Pynput Python library is used for taking input from the system. `pynput.keyboard` is used for recording keystrokes, and `pynput.mouse` can be used to record mouse input. By importing `Listener`, we can record all key inputs from the keyboard.

## Brief Summary of the Main Program
- Imported `Listener` from `pynput`.
- Created a log file (`keylogs.txt`) and stored all string values of key inputs in it.
- Used the `write()` function to save all string values in the log file.
- On key press, it calls the `log_keystrokes` function and records the key input using `Listener`.

## How It Works
After running the program, when a user presses any key on the keyboard, it will call the function and record every keystroke entered by the user until manually stopped via the terminal.

## Running the Keylogger
To run the script normally:
```sh
python keylogger.py
```
To hide it in the background (Windows), change the file extension from `.py` to `.pyw` and run:
```sh
pythonw keylogger.pyw
```

## Possible Improvements
- **Encryption:** Encrypt stored keystrokes for better security.
- **Remote Logging:** Send logs to a remote server via email or webhook.
- **Mouse Logging:** Use `pynput.mouse` to record mouse events.
- **Stealth Mode:** Hide the process from the task manager for a more discreet operation.

## Disclaimer
This project is for educational purposes only. Unauthorized use of keyloggers may violate privacy laws and result in legal consequences. Use responsibly and only with proper authorization.

