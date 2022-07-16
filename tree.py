from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def construct_tree_from_list(data: type[List]) -> Optional[type[TreeNode]]:
    n = len(data)
    if n < 1:
        return TreeNode(None)
    root = TreeNode(data[0])
    q = deque()
    q.append(root)
    cnt = 1
    while len(q) > 0:
        node = q.popleft()
        if node == None:
            continue

        node.left = None if data[cnt] == None else TreeNode(data[cnt])
        cnt += 1
        q.append(node.left)
        if cnt >= n:
            break

        node.right = None if data[cnt] == None else TreeNode(data[cnt])
        cnt += 1
        q.append(node.right)
        if cnt >= n:
            break

    return root


"""
    There are two formats for array form of tree
    1.          1
              /    \
             2       3
            /  \    / \
            X   4   5   X
            /\  /\  / \  /\
           X X 6 7 8  9  X X  

            Array = [1 ,2 ,3 ,None ,4 ,5 ,None ,None ,None ,6 ,7 ,8 ,9 ,None ,None]
    
    2.          1
              /    \
             2       3
            /  \    / \
            X   4   5   X
                /\  / \
                6 7 8  9

            Array = [1 ,2 ,3 ,None ,4 ,5 ,None ,6 ,7 ,8 ,9]
    
    The first one is very redundant form of representation as it assumes the tree to be a full binary tree, while the
    second one does not. The second approach assumes the array to be representation of each level of tree, it skips the 
    none node entirely.
"""
