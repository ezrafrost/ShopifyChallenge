import sys

# Braille dictionary
BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......','capital': '.....O', 'number': '.O.OOO'
}
BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }
# Reverse Braille to English
ENGLISH_LETTERS = {v: k for k, v in BRAILLE_LETTERS.items()}

ENGLISH_NUMBERS = {v: k for k, v in BRAILLE_NUMBERS.items()}

# Check if input is Braille or English
def is_braille(input_str):
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string")
    return len(input_str) % 6 == 0 and set(input_str).issubset({'O', '.'})


def braille_to_english(braille_input):
    result = []
    index = 0
    number_mode = False
    while index < len(braille_input):
        braille_char = braille_input[index:index+6]
        if braille_char == BRAILLE_LETTERS['capital']:
            index += 6
            braille_char = braille_input[index:index+6]
            result.append(ENGLISH_LETTERS[braille_char].upper())
        elif braille_char == BRAILLE_LETTERS['number']:
            number_mode = True
        elif number_mode and braille_char in ENGLISH_NUMBERS:
            result.append(ENGLISH_NUMBERS[braille_char])
        else:
            result.append(ENGLISH_LETTERS.get(braille_char, '?'))
        index += 6
    return ''.join(result)

# Translate English to Braille
def english_to_braille(english_input):
    result = []
    number_mode = False

    for char in english_input:
        if char.isdigit():
            if not number_mode:
                result.append(BRAILLE_LETTERS['number'])
                number_mode = True
            result.append(BRAILLE_NUMBERS[char])
        else:
            if char.isupper():
                result.append(BRAILLE_LETTERS['capital'])
                result.append(BRAILLE_LETTERS[char.lower()])
            else:
                result.append(BRAILLE_LETTERS[char])
            number_mode = False

    return ''.join(result)

def main():
    # Get the input arguments (concatenate them if multiple words are passed)
    input_str = ' '.join(sys.argv[1:])
    
    # Check input and do appropriate translation
    if is_braille(input_str):
        output = braille_to_english(input_str)
    else:
        output = english_to_braille(input_str)
    # Print the output
    print(output)

if __name__ == "__main__":
    main()

