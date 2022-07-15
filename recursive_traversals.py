from tree import TreeNode
from collections import deque


def postorder(node: type[TreeNode]) -> type[list]:
    lst = []

    def helper(node: type[TreeNode]):
        if node == None:
            return
        helper(node.left)
        helper(node.right)
        lst.append(node.val)
        return
    helper(node)
    return lst


def inorder(node: type[TreeNode]) -> type[list]:
    lst = []

    def helper(node: type[TreeNode]):
        if node == None:
            return
        helper(node.left)
        lst.append(node.val)
        helper(node.right)
        return
    helper(node)
    return lst


def preorder(node: type[TreeNode]) -> type[list]:
    lst = []

    def helper(node: type[TreeNode]):
        if node == None:
            return
        lst.append(node.val)
        helper(node.left)
        helper(node.right)
        return
    helper(node)
    return lst


def levelorder(node: type[TreeNode]) -> type[list]:
    traversal = []

    def helper(lst: type[deque]):
        if len(lst) == 0:
            return
        currsize = len(lst)
        for _ in range(currsize):
            node = lst.popleft()
            if node == None:
                continue
            lst.append(node.left)
            lst.append(node.right)
            traversal.append(node.val)
        helper(lst)
        return
    q = deque()
    q.append(node)
    helper(q)
    return traversal
