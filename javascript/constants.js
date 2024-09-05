const braille_dict = {
    "O.....": ["a", "1"],
    "O.O...": ["b", "2"],
    "OO....": ["c", "3"],
    "OO.O..": ["d", "4"],
    "O..O..": ["e", "5"],
    "OOO...": ["f", "6"],
    "OOOO..": ["g", "7"],
    "O.OO..": ["h", "8"],
    ".OO...": ["i", "9"],
    ".OOO..": ["j", "0"],
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
}

const braille_symbols_dict = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "|",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
}

const braille_precursor_dict = {
    ".....O": "capital follows",
    ".O...O": "decimal follows",
    ".O.OOO": "number follows",
    "......": " ",
}

module.exports = { braille_dict, braille_symbols_dict, braille_precursor_dict }