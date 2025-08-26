# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Function to convert text to Morse Code
def text_to_morse(text):
    morse_text = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_text += MORSE_CODE_DICT[char] + ' '
        else:
            morse_text += '? '  # Unknown character
    return morse_text.strip()

# Main Program
def main():
    print("=== Morse Code Converter ===")
    user_input = input("Enter the text you want to convert to Morse Code: ")
    morse_output = text_to_morse(user_input)
    print("\nMorse Code Output:")
    print(morse_output)

if __name__ == "__main__":
    main()
