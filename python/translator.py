import sys

number_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'capital_follows': '.....O', 'number_follows': '.O.OOO'
}

braille_to_number = {x: y for y, x in number_to_braille.items()}
braille_to_english = {x: y for y, x in english_to_braille.items()}

def translate_to_braille(text):
    result = []
    is_num = False

    for char in text:
        if char.isupper():
            result.extend([english_to_braille['capital_follows'], english_to_braille[char.lower()]])
        elif char.isdigit():
            if not is_num:
                is_num = True
                result.append(english_to_braille['number_follows'])
            result.append(number_to_braille[char])
        elif char == ' ':
            is_num = False
            result.append(english_to_braille[' '])
        else:
            result.append(english_to_braille.get(char, ''))

    return ''.join(result)

