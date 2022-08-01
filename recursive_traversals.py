from math import inf
from tree import TreeNode
import bisect
from collections import deque ,OrderedDict


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

def vertical_order(root: type[TreeNode]) -> type[list[list]]:
    # Vorder : {depth : [values]}
    od = OrderedDict()

    def helper(node: type[TreeNode] ,Vorder: int ,depth: int):
        if node is None:
            return
        helper(node.left ,Vorder-1 ,depth+1)
        if Vorder in od.keys():
            if depth in od[Vorder].keys():
                bisect.insort(od[Vorder][depth] ,node.val)
            else:
                od[Vorder][depth] = [node.val]
        else:
            od[Vorder] = OrderedDict()
            od[Vorder][depth] = [node.val]
        helper(node.right ,Vorder+1 ,depth+1)

    helper(root ,0 ,0)
    sol = []
    for k ,v in sorted(od.items()):
        temp = []
        for k ,vl in sorted(v.items()):
            temp += vl
        sol.append(temp)
    return sol