import sys

## Potential problems that should be addressed in a future iteration:

# 1. There is a number-follows character for braille, but there is no letter-follows.
#    Using the current Braille alphabet, it would be impossible to translate some strings.
#    For example, "123abc" can't be translated from neither language without ambiguity using the current rules.
# 2. Exception handling was not specified, so I just raised an exception when an error occurred
#    and gave it the relevant error message.

# This script translates between English text and Braille.
# It includes functions to convert Braille to English and English to Braille.

english_to_braille_main_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O..O.O', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

# Separate dictionary because of the redundancy with letters.
english_to_braille_numbers_dict = {
    '0': '.OOO..','1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Create dicts specifically for the reverse translation. Takes a bit more memory, but keeps searches O(1).  
braille_to_english_main_dict = {v: k for k, v in english_to_braille_main_dict.items()}
braille_to_english_numbers_dict = {v: k for k, v in english_to_braille_numbers_dict.items()}

braille_alphabet = ['O','.']

def translator(*args):
    input = ' '.join(args)
    if is_English(input):
        result = english_to_braille(input)
    else:
        result = braille_to_english(input)
    print(result)

def is_English(text):
    # The logic here is that '.' are not allowed in English as per the current Braille alphabet.
    # Furthermore, every Braille character contains at least one '.'. This verification keeps
    # the language verification O(1).
    if '.' in text[:6]:
        return False
        
    return True


def braille_to_english(braille):
    english_translation = []
    i = 0
    previous_was_number = False
    while i < len(braille):
        if braille[i:i+6] == '......':
            english_translation.append(' ')
            previous_was_number = False

        elif braille[i:i+6] == english_to_braille_main_dict['number']:
            i += 6
            english_translation.append(braille_to_number(braille[i:i+6]))
            previous_was_number = True

        elif previous_was_number:
            english_translation.append(braille_to_number(braille[i:i+6]))

        elif braille[i:i+6] == english_to_braille_main_dict['capital']:
            i += 6
            english_translation.append(braille_to_letter(braille[i:i+6]).upper())
            previous_was_number = False

        else:
            english_translation.append(braille_to_letter(braille[i:i+6]).lower())
            previous_was_number = False

        i += 6
                
    return ''.join(english_translation)

def braille_to_number(braille_segment):
    return braille_to_english_numbers_dict.get(braille_segment, '')

def braille_to_letter(braille_segment):
    return braille_to_english_main_dict.get(braille_segment, '')

def english_to_braille(english):
    braille_translation = []
    previous_char_was = ""

    for char in english:

        if char.isdigit():
            if not (previous_char_was == "number"):
                braille_translation.append(english_to_braille_main_dict['number'])
            braille_translation.append(english_to_braille_numbers_dict[char])
            previous_char_was = "number"

        elif char.isalpha():
            if previous_char_was == "number":
                raise Exception("Invalid input. Cannot have a letter directly after a number under current rules.")
            if char.isupper():
                braille_translation.append(english_to_braille_main_dict['capital'])
                braille_translation.append(english_to_braille_main_dict[char.lower()])

            else:
                braille_translation.append(english_to_braille_main_dict[char])
            
            previous_char_was = "letter"

        elif char == ' ':
            braille_translation.append('......')
            previous_char_was = "space"

        else:
            raise Exception("Invalid input. Character not supported under current rules.")


    return ''.join(braille_translation)



if __name__ == "__main__":
    translator(*sys.argv[1:])
