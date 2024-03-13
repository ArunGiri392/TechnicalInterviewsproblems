class Solution:
    def checkValidString(self, s: str) -> bool:
        # using two stacks.
        # idea.
        # The idea is to put all opening brackets ( in openingbracket stack and star to star stack.
        # if i ever encounter, close bracket, ), then first, i try to , pop from opening bracket to balance.
        # if somehow, opening bracket is empty, then i try to pop from star to make the balance.
        # if both are empty, then, i no, i am in wrong form, so return False.
        
        opening_bracket = []
        star = []

        for i in range(0, len(s)):
            character = s[i]

            if character == "(":
                opening_bracket.append(i)
            
            elif character == "*":
                star.append(i)
            
            else:
                # now we have a closing bracket.
                if opening_bracket:
                    opening_bracket.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        # if i have nothing on opening bracket, then i can directly return true, because even if we have something in star, we can treat as empty string. one of given condition.
        # if not opening_bracket and not star:
        #     return True
        
        # if not opening_bracket and star:
        #     return True

        # These two conditons are commented, becasue the while loop below covers them.
        
        # the reason to put indices. let say, 
        # we have string, (((())** then by end of for loop, openingbracket = [((] and star = [**]
        # so here, start could behave ) and we can get valid parenthis right? 
        # but , 

        # lets say we have this string, **(((()) then by end of for loop, openingbracket = [((] and star = [**] is this valid, not right???
        # so logic here, is, if we have opening bracket after the for loop, so we need to balance with empty string, but the position of this empty string need
        # to come after opening bracket, so we keep track of indices.
        while opening_bracket:
            # if any point, while poping, we reach condition, where, we have opening bracket but our star is empty, then we cannot find the pair, so return False.
            if not star:
                return False
            
            # so index of start > index of opening meaning, * comes later than, opening, then this is valid, then, we can pop both of them.
            elif star[-1] > opening_bracket[-1]:
                star.pop()
                opening_bracket.pop()
            # so index of start < index of opening meaning, * comes before than, opening, then this is not valid, then, we can return False.
            elif star[-1] < opening_bracket[-1]:
                return False
        
        return True

                
        

                
                

