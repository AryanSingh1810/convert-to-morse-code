def save_to_file(text, morse):

    filename = input("Enter filename: ")

    if filename.strip() == "":
        print("Error: Filename cannot be empty.")
        return

    if not filename.endswith(".txt"):
        filename += ".txt"

    with open(filename, "w") as file:

        file.write("English Text:\n")
        file.write(text + "\n\n")

        file.write("Morse Code:\n")
        file.write(morse)

    print("File saved successfully:", filename)


def read_file():

    filename = input("Enter the text filename: ")

    try:

        with open(filename, "r") as file:
            text = file.read()

        return text

    except FileNotFoundError:

        print("Error: File not found.")
        return None

    except Exception as e:

        print("Error:", e)
        return None