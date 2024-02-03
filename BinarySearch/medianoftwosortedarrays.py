class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        A = nums1
        B = nums2
        # we want to keep A as smaller, because we want to do binary search on just 1 array, and we want to do it on smaller array.
        # so making A as smaller array.
        if len(B) < len(A):
            # swapping array to make A as smaller if in case B is the smaller.
            A, B = B, A
        
        left = 0
        right = len(A) - 1

        while True:
            # calculating the point up to where left is taken.
            i = (left + right) // 2
            j = half - i - 2 

            leftA = A[i] if i >= 0 else float("-infinity")
            rightA = A[i + 1] if (i + 1) < len(A) else float("infinity")
            leftB = B[j]  if j >= 0 else float("-infinity")
            rightB = B[j + 1] if (j + 1) < len(B) else float("infinity")
            # if left of A is smaller or equal to then right of B and left of B is smaller thanh or equal to right of A ,
            # then partioning is valid.

            if leftA <= rightB and leftB <= rightA:
                # even case.
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightB, rightA)) / 2
                else:
                    return min(rightA, rightB)
            # here partioning is not valid.
            # if leftA is bigger than rightB. meaning 
            # right b was smaller, meaning our left partioning of A is not valid, so we have to decrease the size of partioning in left side, so bring rigt pointer to i - 1. to make partioning smaller.
            elif leftA > rightB:
                right = i - 1
            # if leftA is smaller than rightB. meaning our left partioning ON A is valid but left partioning on B is not valid,
            # so we wantt o increment the size of the left partioning, in this way, we automatically decrase the length of left partioning of B.
            # right b was smaller, so we have to decrease the size of partioning in left side, so bring rigt pointer to i - 1. to make partioning smaller.
            else:
                left = i + 1

## Time  complexity - log(min(n,m))

