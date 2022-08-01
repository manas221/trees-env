from collections import deque
from tree import TreeNode
from recursive_traversals import inorder

def height(root: type[TreeNode]) -> type[int]:
    if root is None:
        return 0
    return 1 + max(height(root.left) ,height(root.right))

def totalnodes(root: type[TreeNode]) -> type[int]:
    if root is None:
        return 0
    return 1 + totalnodes(root.left) + totalnodes(root.right)

def maxelement(root: type[TreeNode]) -> type[int]:
    return max(inorder(root))

def width(root: type[TreeNode]) -> type[int]:
    if root is None:
        return 0
    # using level order traversal
    q = deque()
    q.append(root)

    maxwidth = 0
    while len(q) > 0:
        currwidth = len(q)
        maxwidth = max(currwidth ,maxwidth)
        for _ in range(currwidth):
            item = q.popleft()
            
            if item.left is not None:
                q.append(item.left)
            if item.right is not None:
                q.append(item.right)
    return maxwidth