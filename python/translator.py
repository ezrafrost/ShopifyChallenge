import sys

english_to_braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', 
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'cap_follows': '.....O', 'dec_follows': '.O...O', 'num_follows': '.O.OOO', '.': '.O..OO',
    ',': '.O....', '?': '.O.OO.', '!': '.OO.O.', ':': 'OO....',
    ';': 'O.O...', '-': '......', '/': 'O.O...', '<': 'O..OO.',
    '>': '.OOO.O', '(': 'OO.OO.', ')': '.OO.OO', ' ': '......',
}

braille_to_english_alphabet = {braille: english for english, braille in english_to_braille_alphabet.items()}


    
print(braille_to_english_alphabet)