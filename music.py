import keyboard
print(keyboard.read_hotkey()); input()

keyboard.add_hotkey("*+-", lambda: keyboard.send("volume up"))
keyboard.add_hotkey("*+plus", lambda: keyboard.send("volume down"))
keyboard.add_hotkey("*+backspace", lambda: keyboard.send("volume mute"))

input()