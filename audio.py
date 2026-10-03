import winsound
import time


def play_morse(morse):

    for symbol in morse:

        if symbol == ".":
            winsound.Beep(800, 150)
            time.sleep(0.05)

        elif symbol == "-":
            winsound.Beep(800, 450)
            time.sleep(0.05)

        elif symbol == " ":
            time.sleep(0.2)

        elif symbol == "/":
            time.sleep(0.5)