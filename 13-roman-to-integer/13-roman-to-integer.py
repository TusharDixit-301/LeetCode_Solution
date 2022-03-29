class Solution:
    def romanToInt(self, s: str) -> int:
        roman_symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        for i in range(0, len(s)):
            Temp = s[i: i+2]
            if len(Temp) == 1 or roman_symbols[Temp[0]] >= roman_symbols[Temp[1]]:
                number += roman_symbols[Temp[0]]
            else:
                number -= roman_symbols[Temp[0]]
        return number