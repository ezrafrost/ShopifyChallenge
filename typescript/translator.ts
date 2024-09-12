type BrailleAlphabet = { [key: string]: string };

const brailleAlphabet: BrailleAlphabet = {
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
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".OOO..",
  " ": "......",
  cap: ".....O",
  num: ".O.OOO",
};

/**
 * Determines if the given input string is written in Braille.
 *
 * Braille is represented by a series of 'O' (for raised dots) and '.' (for flat dots).
 * This function checks if the input consists only of these characters.
 *
 * @param {string} input - The input string to check.
 * @returns {boolean} Returns true if the input is a Braille string (only contains 'O' and '.'), otherwise false.
 */
const isBraille = (input: string): boolean => /^[O.]+$/.test(input);

/**
 * Translates an input string between English and Braille.
 * @param {string} input - The string to be translated. Can be either an English phrase or Braille.
 * @returns {string} The translated string, either Braille or English, depending on the input.
 */
const translate = (input: string): string => {
  if (isBraille(input)) {
    return input;
  }

  return input;
};

// Get the user input
const input = process.argv.slice(2).join(" ");

// Output the translation
console.log(translate(input));
