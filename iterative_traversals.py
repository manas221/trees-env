from tree import TreeNode
from collections import deque


def levelorder(node: type[TreeNode]) -> type[list]:
    """
        DS used : Queue FIFO

        while the queue is not empty:
            get current_size of queue
            for no_of_elements == current_size
            if none skip
            print/store
            append left and right child of queue
    """
    if node == None:
        return []
    traversal = []
    q = deque()
    q.append(node)
    while len(q) > 0:
        currsize = len(q)
        for _ in range(currsize):
            item = q.popleft()
            if item is None:
                continue
            traversal.append(item.val)
            q.append(item.left)
            q.append(item.right)
    return traversal


def inorder(node: type[TreeNode]) -> type[list]:
    """
        DS used : Stack LIFO

        Step 1 : Initialize curr_pointer = root
        Step 2 : while curr_pointer is not none ,do
            push to stack
            curr_pointer = curr_pointer.left
        Step 3: If it is none And stack is NOT EMPTY
            curr_pointer = stack.pop()
            print/store
            curr_pointer = curr_pointer.right
            go to step 2
        Step 4: If it is none and stack is EMPTY, then break and return
    """
    # <left><root><right>
    traversal = []
    curr = node

    stack = deque()

    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif len(stack) > 0:
            curr = stack.pop()
            traversal.append(curr.val)
            curr = curr.right
        else:
            break
    return traversal


def preorder(node: type[TreeNode]) -> type[list]:
    # <root><left><right>
    """
        DS used : Stack LIFO

        While stack is not empty
            -> curr = stack.pop()
            -> if curr is None then continue
            -> print/store
            -> push curr.left
            -> push curr.right
    """
    traversal = []
    curr = node
    stack = deque()

    stack.append(curr)
    while len(stack) > 0:
        curr = stack.pop()
        if curr is not None:
            traversal.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
    return traversal


def postorder(node: type[TreeNode]) -> type[list]:
    # <left><right><root>
    """
        DS used : Stack LIFO

        While stack is not empty
            -> curr = stack.pop()
            -> if curr is None then continue
            -> store in array / stack
            -> push curr.left
            -> push curr.right
        if array then reverse print
        if stack then pop and print
    """
    traversal = []
    st1 = deque()

    def reverse_array():
        i = 0
        j = len(traversal)-1
        while j > i:
            k = traversal[i]
            traversal[i] = traversal[j]
            traversal[j] = k
            j -= 1
            i += 1

    curr = node
    st1.append(curr)
    while len(st1) > 0:
        curr = st1.pop()
        if curr is not None:
            traversal.append(curr.val)
            st1.append(curr.left)
            st1.append(curr.right)

    reverse_array()
    return traversal
