MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}


def convert_to_morse(text):
    result = []

    for letter in text.upper():

        if letter == " ":
            result.append("/")

        elif letter in MORSE_CODE:
            result.append(MORSE_CODE[letter])

        else:
            return None

    return " ".join(result)


def convert_to_english(morse):

    reverse_code = {
        value: key for key, value in MORSE_CODE.items()
    }

    result = []

    words = morse.split(" / ")

    for word in words:

        letters = word.split()

        for letter in letters:

            if letter in reverse_code:
                result.append(reverse_code[letter])

            else:
                return None

        result.append(" ")

    return "".join(result).strip()