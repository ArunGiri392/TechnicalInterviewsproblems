# leetcode 567. Permutaion in string.

# for this question, i traverse through s2 and kept left and right pointer,
#     and if s2[right] in s1, i incremented right and when length of window became length of s1, i returned true.
# does not work!!!!
# let s1 = "abcd" s2 = "aaaaaaaaaaaaa"
#         if s2[r] is always a and a is always present in s1,(hashmap i made), so i cant just check it, may be i have to decrement value of a in hashmap ,or do something.
# but directly checking does not work.

