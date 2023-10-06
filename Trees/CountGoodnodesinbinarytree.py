# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        # # what is hte idea to solve this problem??
        # so basically, for every node we have to find out the numbers in between the path from root node to the particular node.
        # and see if our current node is greater than the all the nodes in path, if yes, it is a good node, else not.

        # so how to find the numbers in that path? but do we need to keep track of all the numbers in that path?
        # what if we just keep track of maximum number in that path and compare it with our current number such that, we could compare current number with the maximum number in that path.
        # so wee kepp on tracking the maximum number in that path. ie on every node level. and recursively call .

        # we createa dfs functon which takes the node and the maximum value. initally, our root node is itself the max value and root nodes value will be equlat to or grater han the max value, so it works.

        # after this we recursivlely, go on every level, and check the condition and also update the max we have encoutnererd this far.

        # one thing here, lets say , we haev a max in left side, so can we use the same max on different path? not?
        # so that is why calcualte max at every level, and every function on call stack will hold the node value and max value, so we know the max value at every level.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes  = 0

        def dfs(root, max_value):
            nonlocal good_nodes
            if root == None:
                return
            if root.val >= max_value:
                good_nodes += 1
            max_value = max(max_value, root.val)
            dfs(root.left, max_value)
            dfs(root.right, max_value)
            return

        

        dfs(root,root.val)
        return good_nodes

# Time complextiy - o(n) WHERE N is the no of nodes in the binary tree.
# Space complexity - o(N) in the worst case, if there is skewed tree, we wll have N number of function on the call stack such that the height of the call stack will be equal to no of nodes.