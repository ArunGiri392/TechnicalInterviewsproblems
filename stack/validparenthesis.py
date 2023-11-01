class Solution(object):
    def isValid(self, s):
        opening = { "(","[","{" }
        stack = []
        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                poped_bracket = stack.pop()
                if bracketauthenticator(poped_bracket, bracket) == False:
                    return False
        if len(stack) != 0:
            return False
        return True
    
def bracketauthenticator(openingbracket, closingbracket):
    if openingbracket == "(" and closingbracket == ")":
        return True
    elif openingbracket == "{" and closingbracket == "}":
        return True
    elif openingbracket == "[" and closingbracket == "]":
        return True
    return False