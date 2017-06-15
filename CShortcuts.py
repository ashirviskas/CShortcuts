import pyperclip
import time
import json

DEFAULT_SHORTCUTS_FILENAME = "default_shortcuts.json"


def read_shortcuts_from_file(filename):
    json_data=open(filename, "r").read()
    shortcuts_ = json.loads(json_data)
    return shortcuts_


if __name__ == "__main__":
    default_shortcuts = read_shortcuts_from_file(DEFAULT_SHORTCUTS_FILENAME)
    while True:
        copied = pyperclip.paste()
        if copied in default_shortcuts:
            pyperclip.copy(default_shortcuts[copied])
        time.sleep(0.05)

