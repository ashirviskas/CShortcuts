import pyperclip
import time

shortcuts = {}
shortcuts["b"] = "I'm glad I could help you, have a nice day!"
shortcuts["apl"] = "If you're using Apple AirPort, follow these instructions: \n https://support.getcujo.com/support/solutions/articles/9000092004-dhcp-mode-apple-airport "


if __name__ == "__main__":
    while True:
        copied = pyperclip.paste()
        if copied in shortcuts:
            pyperclip.copy(shortcuts[copied])
        time.sleep(0.05)

