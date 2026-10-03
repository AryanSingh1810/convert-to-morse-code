import tkinter as tk
from tkinter import messagebox, filedialog

from morse_converter import convert_to_morse, convert_to_english
from audio import play_morse
from file_handler import save_to_file
from history import save_history, show_history, clear_history


def start_gui():

    window = tk.Tk()

    window.title("Morse Code Converter")
    window.geometry("700x600")
    window.resizable(False, False)

    # Title
    title = tk.Label(
        window,
        text="MORSE CODE CONVERTER",
        font=("Arial", 24, "bold")
    )

    title.pack(pady=20)

    # Input Label
    input_label = tk.Label(
        window,
        text="Enter Text / Morse Code",
        font=("Arial", 14)
    )

    input_label.pack()

    # Input Box
    input_box = tk.Text(
        window,
        height=7,
        width=70,
        font=("Arial", 12)
    )

    input_box.pack(pady=10)

    # Output Label
    output_label = tk.Label(
        window,
        text="Output",
        font=("Arial", 14)
    )

    output_label.pack()

    # Output Box
    output_box = tk.Text(
        window,
        height=7,
        width=70,
        font=("Arial", 12)
    )

    output_box.pack(pady=10)


    def english_to_morse():

        text = input_box.get("1.0", tk.END).strip()

        if text == "":
            messagebox.showerror(
                "Error",
                "Input cannot be empty."
            )
            return

        result = convert_to_morse(text)

        if result is None:

            messagebox.showerror(
                "Error",
                "Unsupported character found."
            )

            return

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

        save_history(
            text,
            result,
            "English → Morse"
        )


    def morse_to_english():

        morse = input_box.get("1.0", tk.END).strip()

        if morse == "":
            messagebox.showerror(
                "Error",
                "Morse code cannot be empty."
            )
            return

        result = convert_to_english(morse)

        if result is None:

            messagebox.showerror(
                "Error",
                "Invalid Morse code found."
            )

            return

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

        save_history(
            morse,
            result,
            "Morse → English"
        )


    def play_sound():

        morse = output_box.get(
            "1.0",
            tk.END
        ).strip()

        if morse == "":
            messagebox.showerror(
                "Error",
                "No Morse code available."
            )
            return

        try:

            play_morse(morse)

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )


    def save_result():

        text = input_box.get(
            "1.0",
            tk.END
        ).strip()

        morse = output_box.get(
            "1.0",
            tk.END
        ).strip()

        if text == "" or morse == "":
            messagebox.showerror(
                "Error",
                "Nothing to save."
            )
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        if filename == "":
            return

        try:

            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:

                file.write("English Text:\n")
                file.write(text)
                file.write("\n\n")

                file.write("Morse Code:\n")
                file.write(morse)

            messagebox.showinfo(
                "Success",
                "File saved successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )


    def load_file():

        filename = filedialog.askopenfilename(
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        if filename == "":
            return

        try:

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:

                text = file.read()

            input_box.delete("1.0", tk.END)
            input_box.insert(tk.END, text)

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )


    def view_history():

        try:

            with open(
                "history.txt",
                "r",
                encoding="utf-8"
            ) as file:

                history = file.read()

            if history.strip() == "":
                history = "History is empty."

        except FileNotFoundError:

            history = "No history found."

        history_window = tk.Toplevel(window)

        history_window.title("Conversion History")
        history_window.geometry("700x400")

        history_box = tk.Text(
            history_window,
            font=("Arial", 11)
        )

        history_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        history_box.insert(
            tk.END,
            history
        )

        history_box.config(
            state="disabled"
        )


    def clear_history_gui():

        clear_history()

        messagebox.showinfo(
            "History",
            "History cleared successfully."
        )


    # Buttons

    button_frame = tk.Frame(window)
    button_frame.pack(pady=15)

    english_button = tk.Button(
        button_frame,
        text="English → Morse",
        width=18,
        command=english_to_morse
    )

    english_button.grid(
        row=0,
        column=0,
        padx=5,
        pady=5
    )


    morse_button = tk.Button(
        button_frame,
        text="Morse → English",
        width=18,
        command=morse_to_english
    )

    morse_button.grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )


    sound_button = tk.Button(
        button_frame,
        text="Play Sound",
        width=18,
        command=play_sound
    )

    sound_button.grid(
        row=0,
        column=2,
        padx=5,
        pady=5
    )


    save_button = tk.Button(
        button_frame,
        text="Save File",
        width=18,
        command=save_result
    )

    save_button.grid(
        row=1,
        column=0,
        padx=5,
        pady=5
    )


    load_button = tk.Button(
        button_frame,
        text="Load Text File",
        width=18,
        command=load_file
    )

    load_button.grid(
        row=1,
        column=1,
        padx=5,
        pady=5
    )


    history_button = tk.Button(
        button_frame,
        text="View History",
        width=18,
        command=view_history
    )

    history_button.grid(
        row=1,
        column=2,
        padx=5,
        pady=5
    )


    clear_button = tk.Button(
        button_frame,
        text="Clear History",
        width=18,
        command=clear_history_gui
    )

    clear_button.grid(
        row=2,
        column=1,
        padx=5,
        pady=5
    )


    window.mainloop()


if __name__ == "__main__":
    start_gui()