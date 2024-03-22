def merge_sort(array):
    # if at point, length of array becomes 1, return
    if len(array) == 1:
        return

    mid = len(array) // 2
    left = array[0: mid]
    right = array[mid: ]

    merge_sort(left)
    merge_sort(right)
    

    i = 0
    j = 0
    # k pointer points to the original array . i points to left array and j points to the right array.
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1 
    
    while i < len(left):
         array[k] = left[i]
         i += 1
         k += 1
    
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

my_array = [38, 27, 43, 3, 9, 82, 10]
my_array2 = [-2,3,-5]
merge_sort(my_array)
merge_sort(my_array2)
print("Sorted array:", my_array)
print("Sorted array:", my_array2)

# Time complexity - o(N * LOG(N)) becuase to divide it takes log(N) work, and later, for each division , we are mergint two arrays, w
# which is a o(N) work , so that makes o(N * LOG(N))

# space complexity - at worst case, the height of the stack for recursiong becomes o(logn) 
# but we are using two temprary arrays, left and right, and on worst case their lenght might be equal to o(n/2) so that 
# makes overall time complexity as O(n)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left = nums[0:mid]
        right = nums[mid: ]

        self.sortArray(left)
        self.sortArray(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
        return nums
        
# Time complexity - o(nlogn)
#space complexity - o(N)
            