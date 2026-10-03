from morse_converter import convert_to_morse, convert_to_english
from audio import play_morse
from file_handler import save_to_file, read_file
from history import save_history, show_history, clear_history
from gui import start_gui


start_gui()

while True:

    print("\n===== MORSE CODE CONVERTER =====")

    print("1. English → Morse")
    print("2. Morse → English")
    print("3. Play Morse Sound")
    print("4. Save Morse Code to File")
    print("5. Convert Text File → Morse")
    print("6. View History")
    print("7. Clear History")
    print("8. Exit")

    choice = input("\nEnter your choice: ")


    # English → Morse
    if choice == "1":

        text = input("Enter English text: ")

        if text.strip() == "":
            print("Error: Input cannot be empty.")

        else:

            result = convert_to_morse(text)

            if result is None:
                print("Error: Unsupported character found.")

            else:

                print("\nMorse Code:")
                print(result)

                save_history(
                    text,
                    result,
                    "English → Morse"
                )


    # Morse → English
    elif choice == "2":

        morse = input("Enter Morse Code: ")

        if morse.strip() == "":
            print("Error: Morse code cannot be empty.")

        else:

            result = convert_to_english(morse)

            if result is None:
                print("Error: Invalid Morse code found.")

            else:

                print("\nEnglish:")
                print(result)

                save_history(
                    morse,
                    result,
                    "Morse → English"
                )


    # Play Morse Sound
    elif choice == "3":

        text = input("Enter English text for sound: ")

        if text.strip() == "":
            print("Error: Input cannot be empty.")

        else:

            morse = convert_to_morse(text)

            if morse is None:

                print("Error: Unsupported character found.")

            else:

                print("\nMorse Code:")
                print(morse)

                print("\nPlaying Morse sound...")

                play_morse(morse)

                print("Sound finished.")


    # Save Morse Code
    elif choice == "4":

        text = input("Enter English text: ")

        if text.strip() == "":
            print("Error: Input cannot be empty.")

        else:

            morse = convert_to_morse(text)

            if morse is None:

                print("Error: Unsupported character found.")

            else:

                print("\nMorse Code:")
                print(morse)

                save_to_file(text, morse)


    # Convert Text File → Morse
    elif choice == "5":

        text = read_file()

        if text is not None:

            if text.strip() == "":
                print("Error: File is empty.")

            else:

                morse = convert_to_morse(text)

                if morse is None:

                    print(
                        "Error: File contains unsupported characters."
                    )

                else:

                    print("\nEnglish Text:")
                    print(text)

                    print("\nMorse Code:")
                    print(morse)

                    save_to_file(text, morse)

    elif choice == "6":

     show_history()


    elif choice == "7":

     clear_history()


    elif choice == "8":

     print("\nThank you for using Morse Code Converter!")

    break


else:

    print("Error: Invalid choice.")