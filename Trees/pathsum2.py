# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# This problem is an eye opener for me and it introduces me to the world of Backtracking.
# Remember, in the path sum 1, problem, i made use of variable. but in this problem,i have to make use of list.
# and remember, list is a mutable meaning they are passed by reference, meaning when they are passed as an argument , they are passed by their reference, and copy is not proivded,meaning, any changes you make to that state(list) will also affect the original list.

# so that is the reason you have to pop, to make sure, when you reach to the initial stage, make sure,your list is up to date.
# if you do not do pop,and when you come to initial stage, you list might have been updated due to other operations you did earlier.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(root, array): 
            if root == None:
                return
            
            array.append(root.val)

            if root.left == None and root.right == None:
                if sum(array) == targetSum:
                    result.append(array.copy())
                    # array.pop()
                return
            
            if root.left:
                dfs(root.left, array)
                array.pop()
            
            if root.right:
                dfs(root.right, array)
                array.pop()
            return

            
        dfs(root, [])
        return result

        
    
# The reason why we dont add currentlist directly and have to add the copy of the current list?
                    # lets imagine, i added the real current list in the finallist array.
                    # and later i made changed to currentlist variable, then those changeswill  also be reflected in the currentlist array inside the finallist array.
                    # so to make them independent of each other, i add the copy of current list such that i can continue to work on the current list and any  changes made to current list willnot affect the copy of the curren list i inserted in the final list.
# When you do list(current_list), you're creating a new copy of current_list. The purpose of this is to save the current state of current_list as a separate object in final_list.

# If you just did final_list.append(current_list) without creating a new copy, you'd be appending a reference to current_list. Remember that lists in Python are mutable and passed by reference. This means that any changes you make to current_list in subsequent operations (like the pop() operation for backtracking) would be reflected in all the references to that list in final_list.

# By creating a new copy using list(current_list), you ensure that the version of current_list you append to final_list is independent of the current_list you continue to modify in your function.