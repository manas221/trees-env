from collections import deque
from tree import TreeNode



def right_view_recursive(root: type[TreeNode]) -> type[list]:
    """
        Recursive solution

        Intution : Rightmost view is the collection of first node from the 
                   right at each level
                   We can go for reverse postorder traversal (<root><right>left)
                   ,this will help in moving to right tree first and print the root
                   and same again for lower levels.
                   To only print the righmost element, we keep a level counter and 
                   print only once whenever the counter increases

        code uses length of right_view_nodes as the level indicator upto which 
        view is found ,for eg. root is at 0th level, and func is intialized at 0
        so print that and increase counter, the next element would be rightmost
        element at first level ,print it and increment counter and so on..
    """
    right_view_nodes = []

    def helper(node: type[TreeNode], level_counter: int):
        if node is None:
            return
        if level_counter == len(right_view_nodes):
            right_view_nodes.append(node.val)
        helper(node.right, level_counter+1)
        helper(node.left, level_counter+1)
        return

    helper(root, 0)
    return right_view_nodes


def left_view_recursive(root: type[TreeNode]) -> type[list]:
    """
        Recursive solution

        Intution : LeftMost view is the collection of first node from the 
                   left at each level
                   We can go for  postorder traversal (<root><left><right>)
                   ,this will move to left tree(where we wanna go) and due to nature
                   the node at leftmost will be reached first in that level as tree is traversed
                   left to right.
                   Additionally a counter to tracke level is required so as to print only the first 
                   element

        code uses length of left as the level indicator upto which 
        view is found ,for eg. root is at 0th level, and func is intialized at 0
        so print that and increase counter, the next element would be leftmost
        element at first level ,print it and increment counter and so on..
    """
    left = []

    def helper(node: type[TreeNode] ,level_counter: int):
        if node is None:
            return
        if level_counter == len(left):
            left.append(node.val)
        helper(node.left ,level_counter+1)
        helper(node.right ,level_counter+1)
        return
    helper(root ,0)
    return left

"""
    for iterative approaches in left and right view,it is just level order traversal
    and print either leftmost or rightmost element, from queue,
    but it's space complexity is very expensive

    Also ,recursive approaches become too complicated for top view as sometimes if tree
    has more nodes on either side, then the algorithm fails as the vertical order is reached first. 
    So, iterative(level order is best used)
"""

def top_view_iterative(root: type[TreeNode]) -> type[list]:
    '''
        A priority queue and level order traversal(which is implemented quite differently than I expected)
        Based on Striver's video
    '''
    ans = []
    if root is None:
        return ans
    mpp = {}
    q = deque()
    q.append((root ,0))
    while len(q) > 0:
        node ,line = q.popleft() 
        if line not in mpp.keys():
            mpp[line] = node.val
        
        if node.left is not None:
            q.append((node.left ,line-1))
        if node.right is not None:
            q.append((node.right ,line+1))

    for k ,v in mpp.items():
        ans.append(v)
    return ans