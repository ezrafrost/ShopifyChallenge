#!/usr/bin/env node

const alphabet = [
  {
    br: "O.....",
    en: "a",
    num: 1,
  },
  {
    br: "O.O...",
    en: "b",
    num: 2,
  },
  {
    br: "OO....",
    en: "c",
    num: 3,
  },
  {
    br: "OO.O..",
    en: "d",
    num: 4,
  },
  {
    br: "O..O..",
    en: "e",
    num: 5,
  },
  {
    br: "OOO...",
    en: "f",
    num: 6,
  },
  {
    br: "OOOO..",
    en: "g",
    num: 7,
  },
  {
    br: "O.OO..",
    en: "h",
    num: 8,
  },
  {
    br: ".OO...",
    en: "i",
    num: 9,
  },
  {
    br: ".OOO..",
    en: "j",
    num: 0,
  },
  {
    br: "O...O.",
    en: "k",
  },
  {
    br: "O.O.O.",
    en: "l",
  },
  {
    br: "OO..O.",
    en: "m",
  },
  {
    br: "OO.OO.",
    en: "n",
  },
  {
    br: "O..OO.",
    en: "o",
  },
  {
    br: "OOO.O.",
    en: "p",
  },
  {
    br: "OOOOO.",
    en: "q",
  },
  {
    br: "O.OOO.",
    en: "r",
  },
  {
    br: ".OO.O.",
    en: "s",
  },
  {
    br: ".OOOO.",
    en: "t",
  },
  {
    br: "O...OO",
    en: "u",
  },
  {
    br: "O.O.OO",
    en: "v",
  },
  {
    br: ".OOO.O",
    en: "w",
  },
  {
    br: "OO..OO",
    en: "x",
  },
  {
    br: "OO.OOO",
    en: "y",
  },
  {
    br: "O..OOO",
    en: "z",
  },
  {
    br: "..OO.O",
    en: ".",
  },
  {
    br: "..O...",
    en: ",",
  },
  {
    br: "..O.OO",
    en: "?",
  },
  {
    br: "..OOO.",
    en: "!",
  },
  {
    br: "..OO..",
    en: ":",
  },
  {
    br: "..O.O.",
    en: ";",
  },
  {
    br: "....OO",
    en: "-",
  },
  {
    br: ".O..O.",
    en: "/",
  },
  {
    br: ".OO..O",
    en: "<",
  },
  {
    br: "O..OO.",
    en: ">",
  },
  {
    br: "O.O..O",
    en: "(",
  },
  {
    br: ".O.OO.",
    en: ")",
  },
  {
    br: "......",
    en: " ",
  },
];

function isBraille(string) {
  if (string.length % 6 !== 0) {
    return false;
  } else {
    for (const char of string) {
      if (!(char === "O" || char === ".")) {
        return false;
      } else {
        return true;
      }
    }
  }
}

console.log(isBraille("hello "));
