HISTORY_FILE = "history.txt"


def save_history(original, converted, direction):

    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as file:
            file.write(
                f"{direction}: {original} -> {converted}\n"
            )

    except Exception as e:
        print("Error saving history:", e)


def show_history():

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = file.read()

        if history.strip() == "":
            print("\nHistory is empty.")

        else:
            print("\n===== CONVERSION HISTORY =====")
            print(history)

    except FileNotFoundError:
        print("\nNo history found.")


def clear_history():

    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            file.write("")

        print("\nHistory cleared successfully.")

    except Exception as e:
        print("Error clearing history:", e)