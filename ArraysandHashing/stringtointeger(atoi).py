
class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        result = 0
        sign = 1
        # strip function removes " "ie leading spaces from front and back. does not remove from the middle.
        stripped_string = s.strip()

        if not stripped_string:
            return 0

        next_character = stripped_string[0]
        if next_character == "-":
            start = 1
            sign = -1
        elif next_character == "+":
            start = 1
        else:
            start = 0

        for i in range(start, len(stripped_string)):
            char = stripped_string[i]
            if char not in "0123456789":
                break
            else:
                result = result * 10 + int(char)
        
    

        if sign == 1:
            if result > 2**31 - 1:
                return 2**31 - 1
            return result

        elif sign == -1:
            if -1 * result < -2**31 :
                return -2**31 
            return -1 * result
        