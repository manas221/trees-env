
from tree import TreeNode
import bisect
from collections import deque, OrderedDict


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

def vertical_order(root: type[TreeNode]) -> type[list[list]]:
    q = deque()

    # Vorder : {depth : [values]}
    od = OrderedDict()
    q.append((root ,0 ,0))
    while len(q) > 0:
        item ,Vorder ,depth = q.popleft()
        if item is None:
            continue
        q.append((item.left ,Vorder-1 ,depth+1))
        q.append((item.right ,Vorder+1 ,depth+1))
        
        if Vorder in od.keys():
            if depth in od[Vorder].keys():
                bisect.insort(od[Vorder][depth] ,item.val)
            else:
                od[Vorder][depth] = [item.val]
        else:
            od[Vorder] = OrderedDict()
            od[Vorder][depth] = [item.val]
    sol = []
    for k ,v in sorted(od.items()):
        temp = []
        for k ,vl in sorted(v.items()):
            temp += vl
        sol.append(temp)
    return sol

def spiral_order_queue(root: type[TreeNode]) -> type[list]:
    spiral = []
    
    qleft = deque()    # l2r
    qright = deque()   # r2l
    flag = 0    # 0 l2r ,1 r2l
    qleft.append(root)
    while len(qleft) > 0 or len(qright) > 0:
        if flag == 0:
            currlen = len(qleft)
            for _ in range(currlen):
                node = qleft.popleft()
                if node is None:
                    continue
                spiral.append(node.val)
                # print(node.val)
                qright.append(node.left)
                qright.append(node.right)
            flag = 1
        if flag == 1:
            currlen = len(qright)
            for _ in range(currlen):
                node = qright.pop()
                if node is None:
                    continue
                spiral.append(node.val)
                # print(node.val)
                qleft.appendleft(node.right)
                qleft.appendleft(node.left)
            flag = 0
    return spiral
    
def sprial_order_stacks(root: type[TreeNode]) -> type[list]:
    spiral = []

    stleft = deque()
    stright = deque()

    stleft.append(root)
    flag = 0

    while len(stleft) > 0 or len(stright) > 0:
        if flag == 0:
            while len(stleft) > 0:
                node = stleft.pop()
                if node is None:
                    continue
                spiral.append(node.val)
                stright.append(node.left)
                stright.append(node.right)
            flag = 1
        if flag == 1:
            while len(stright) > 0:
                node = stright.pop()
                if node is None:
                    continue
                spiral.append(node.val)
                stleft.append(node.right)
                stleft.append(node.left)
            flag = 0
    return spiral