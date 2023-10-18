def is_full_tree(root):
    if root == None:
        return True
    left = is_full_tree(root.left)
    right = is_full_tree(root.right)

    if root.left and root.right:
        current = True
        
    if root.left == None or root.right == None:
        current = False
    
    if root.left == None and root.right == None:
        current = True
    return (left and right) and current
