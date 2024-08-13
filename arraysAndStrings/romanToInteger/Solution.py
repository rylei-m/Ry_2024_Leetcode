class Solution:
    def romanToInt(self, s: str) -> int:
        numeral = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        su = 0
        n = len(s)
        i = 0

        while i < n:
            if i < n - 1 and numeral[s[i]] < numeral[s[i + 1]]:
                su += numeral[s[i + 1]] - numeral[s[i]]
                i += 2
            else:
                su += numeral[s[i]]
                i += 1
        return su


Tests = [
    "MCMXCIV",
    "LVIII",
    "XIV",
    "XXX",
]
