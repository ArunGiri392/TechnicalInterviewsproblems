class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # if any triplet at certain index has value greater than the value at target at same index, we know , this triplet can never be part of answer. so dont consider it.
        # now, the remaining value in tripet has value less than or equal to triplet. so if we want to create a tripelt from the remaining one, 
        # the, for each triplet in target, for each index, we need to have same element at same index, at triplets we have, 
        # if we can find, all the triplets from the target of aech index, at triplet given, then we can say, in someway, we will for sure be able to get the result target.
        good = set()

        for triplet in triplets:
            # filtering not pissible target.
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i in range(0, 3):
                # chekcing if we can target element at each index, if it is present in triplet.
                if triplet[i] == target[i] and i not in good:
                    good.add(i)
            
        return len(good) == 3
