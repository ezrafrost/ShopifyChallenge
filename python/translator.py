BRAILLE_TO_CHARACTER = {
    "O.....": "a", "O.O...": "b", "OO....": "c",
    "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i",
    ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", "......": " ",
}

BRAILLE_TO_DIGIT = {
    "O.....": "1", "O.O...": "2", "OO....": "3",
    "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
    ".OOO..": "0",
}

CHARACTER_TO_BRAILLE = {char: braille_char for braille_char, char in BRAILLE_TO_CHARACTER.items()}
DIGIT_TO_BRAILLE = {digit: braille_char for braille_char, digit in BRAILLE_TO_DIGIT.items()}

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = CHARACTER_TO_BRAILLE[" "]