# Morse Code Converter

A Python-based Morse Code Converter that allows users to convert **English text to Morse code** and **Morse code back to English**.

The project started as a command-line application and was extended with a **Tkinter graphical user interface**, Morse audio playback, file handling, conversion history, and error handling.

---

## 🚀 Features

* 🔤 English → Morse Code
* 🔄 Morse Code → English
* 🔢 Support for numbers
* ✍️ Support for punctuation and special characters
* 🔊 Play Morse Code as audio
* 💾 Save conversions to `.txt` files
* 📂 Load text files
* 📜 Store and view conversion history
* 🗑️ Clear conversion history
* 📋 Copy output to clipboard
* ⇅ Swap input and output
* 🧹 Clear input and output
* ⚠️ Input validation and error handling
* 🖥️ Modern Tkinter desktop GUI

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter** — Graphical User Interface
* **winsound** — Morse audio playback on Windows
* **File Handling** — Saving and reading `.txt` files
* **Dictionary** — Morse code mapping
* **Functions** — Modular program structure
* **Exception Handling** — Error management

---

## 📁 Project Structure

```text
MorseCodeConverter/
│
├── main.py
├── gui.py
├── morse_converter.py
├── audio.py
├── file_handler.py
├── history.py
├── history.txt
└── README.md
```

### File Description

| File                 | Purpose                                         |
| -------------------- | ----------------------------------------------- |
| `main.py`            | Starts the application                          |
| `gui.py`             | Contains the Tkinter graphical interface        |
| `morse_converter.py` | Contains English ↔ Morse conversion logic       |
| `audio.py`           | Plays Morse code as sound                       |
| `file_handler.py`    | Handles reading and writing text files          |
| `history.py`         | Stores, displays, and clears conversion history |
| `history.txt`        | Stores previous conversions                     |
| `README.md`          | Project documentation                           |

---

## 📌 Supported Morse Code

### Alphabets

```text
A  .-
B  -...
C  -.-.
D  -..
E  .
F  ..-.
G  --.
H  ....
I  ..
J  .---
K  -.-
L  .-..
M  --
N  -.
O  ---
P  .--.
Q  --.-
R  .-.
S  ...
T  -
U  ..-
V  ...-
W  .--
X  -..-
Y  -.--
Z  --..
```

### Numbers

```text
0  -----
1  .----
2  ..---
3  ...--
4  ....-
5  .....
6  -....
7  --...
8  ---..
9  ----.
```

### Common Punctuation

The converter also supports characters such as:

```text
.  ,  ?  !  '  /  (  )
&  :  ;  =  +  -
_  "  $  @
```

---

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the installation using:

```powershell
python --version
```

---

### 2. Open the Project Folder

Open PowerShell or the VS Code terminal and navigate to the project folder.

Example:

```powershell
cd "C:\Users\aryan\OneDrive\Documents\morse code"
```

---

### 3. Run the Application

Run:

```powershell
python main.py
```

The Morse Code Converter GUI should open.

---

## 🖥️ How to Use

### English → Morse

Enter English text in the input box.

Example:

```text
HELLO WORLD
```

Click:

```text
English → Morse
```

Output:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

---

### Morse → English

Enter Morse code:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

Click:

```text
Morse → English
```

Output:

```text
HELLO WORLD
```

---

### 🔊 Play Morse Sound

After converting English text to Morse code, click:

```text
▶ Play Sound
```

The application uses different sound durations for dots and dashes.

* Dot `.` → Short sound
* Dash `-` → Long sound

---

### 💾 Save File

Click:

```text
Save File
```

Choose a location and filename.

The application saves both the input and output.

Example:

```text
Input:
HELLO WORLD

Output:
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

---

### 📂 Load File

Click:

```text
Load File
```

Select a `.txt` file.

The contents will be loaded into the input box.

---

### 📜 View History

Every successful conversion is stored in:

```text
history.txt
```

Click:

```text
History
```

to view previous conversions.

---

### 📋 Copy Output

Click:

```text
Copy
```

to copy the converted result to the clipboard.

---

### ⇅ Swap

The `Swap` functionality allows you to exchange the contents of the input and output boxes.

---

### 🗑️ Clear History

Click:

```text
Clear History
```

to remove previously stored conversion history.

---

## 🧠 How the Converter Works

The application uses a Python dictionary to store Morse code mappings.

Example:

```python
MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..'
}
```

For English → Morse conversion, each character is searched in the dictionary.

For Morse → English conversion, the dictionary is reversed:

```python
reverse_code = {
    value: key
    for key, value in MORSE_CODE.items()
}
```

This allows the program to find the English character corresponding to a Morse sequence.

---

## 📊 Example

### Input

```text
Hello, World!
```

### Morse Output

```text
.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--
```

### Reverse Conversion

```text
HELLO, WORLD!
```

---

## ⚠️ Error Handling

The application handles common errors such as:

* Empty input
* Unsupported characters
* Invalid Morse code
* Missing files
* File reading errors
* File writing errors
* Empty history

Example:

```text
Error: Input cannot be empty.
```

---

## 🔮 Future Improvements

Possible future versions can include:

* 🌐 Web version
* 📱 Mobile version
* 🎨 More advanced GUI design
* 🌙 Dark/Light theme switch
* 🎚️ Adjustable Morse sound speed
* 📊 Conversion statistics
* 🔐 Morse code encryption/decryption
* 🗣️ Speech-to-Morse conversion
* 🔊 Morse-to-speech conversion
* 📦 Windows `.exe` application
* ⌨️ Keyboard shortcuts
* 🌍 Support for additional languages

---

## 🎯 Learning Objectives

This project demonstrates practical use of:

* Python dictionaries
* Functions
* Loops
* Conditional statements
* File handling
* Exception handling
* Modular programming
* GUI development with Tkinter
* Audio processing
* User input validation
* Basic software project structure

---

## 👨‍💻 Author

**Aryan Singh**

B.Tech CSE — AI & ML

---

## 📄 License

This project is created for educational and learning purposes.
