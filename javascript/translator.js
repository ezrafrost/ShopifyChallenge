// Mappings for English to Braille Translation
const englishToBraille = {
    a: "O.....",
    b: "O.O...",
    c: "OO....",
    d: "OO.O..",
    e: "O..O..",
    f: "OOO...",
    g: "OOOO..",
    h: "O.OO..",
    i: ".OO...",
    j: ".OOO..",
    k: "O...O.",
    l: "O.O.O.",
    m: "OO..O.",
    n: "OO.OO.",
    o: "O..OO.",
    p: "OOO.O.",
    q: "OOOOO.",
    r: "O.OOO.",
    s: ".OO.O.",
    t: ".OOOO.",
    u: "O...OO",
    v: "O.O.OO",
    w: ".OOO.O",
    x: "OO..OO",
    y: "OO.OOO",
    z: "O..OOO",
    " ": "......",
    CAPITAL: ".....O",
    NUMBER: ".O.OOO",
};

const numberToBraille = {
    0: ".OOO..",
    1: "O.....",
    2: "O.O...",
    3: "OO....",
    4: "OO.O..",
    5: "O..O..",
    6: "OOO...",
    7: "OOOO..",
    8: "O.OO..",
    9: ".OO...",
};

// Reverse mappings
const brailleToEnglish = {};
for (const [key, value] of Object.entries(englishToBraille)) {
    if (key !== "CAPITAL" && key !== "NUMBER") {
        brailleToEnglish[value] = key;
    }
}

const brailleToNumber = {};
for (const [key, value] of Object.entries(numberToBraille)) {
    brailleToNumber[value] = key;
}

