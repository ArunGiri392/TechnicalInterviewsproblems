# adding number ie length of string infront
# becuse the length of the string will help us to slice the string of that length.

        # also adding any deliminator (#) in front 
        # why addiding deliminator? would not length be sufficient.(to avoid confusion with the number)
        # "1234" -- 4e here it can esailt decode.
        # "1234567890" - 10 1234567890, so now how would you differentiate wheter
        # length of string is 1 or 10 , during encoding,
        # so adding, # after length helps us to know the length

def encode (self, strs: List[str]) -> str:
    res = ""
    for string in strs:
        res += str(len(string)) + "#" + string
    return res
        





def decode(self, s: str) -> List[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int (s[ i : j])
        result.append(s[j + 1 : j + 1 +  length])
        i = j + 1 + length 

    return result

            