# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return 
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        # print(",".join(res))
        return ",".join(res)
        # # to not get confused with -negative nums, we add , in between numbers.
        # if i had 3 and -7, then, string would be 3-7 (if there was no comma)
        # so comma create distinction betwen numbers ie, 3, -7, so add comma betwen every numbers.

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # now here we have string , may be in this format, "1,-2,-5,7"
        # so if we just iterate through this, we also iterate through , and -, as loop takes everythnng.
        # so convert this into list, meaning, split these on commas, such that list is ["1", "-2", "-5", "-7"]
       
        vals = data.split(",")
        
        # i is defined as global here.
        i = 0

        def dfs():
            nonlocal i
            if vals[i] == "N":
                # if somehow, we come here, then , and if we do not increase index, for same, index, we would do .root.left, and root.right,
                # so increasing index is necessary.
                i += 1
                return None
            
            root = TreeNode(int(vals[i]))
            # once we create a node from this index, we want to get another index, so, increase it.
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))