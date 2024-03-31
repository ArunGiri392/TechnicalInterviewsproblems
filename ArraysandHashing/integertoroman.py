class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        # There are only six instances where subtraction is used.
        # so, we just add this instances in our roman numerals list.
        # for 49 -- 40 + 9 (XLIX)
        roman = ""
        for data in roman_numerals:
            number = data[0]
            roman_sign = data[1]
            while num >= number:
                roman += roman_sign
                num -= number
        return roman
# Time complexity - o(N)
# space complexity - o(1)