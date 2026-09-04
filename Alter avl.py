# C++ program to find number of elements
# greater than a given value in AVL


# Python code

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.desc = 0


def height(N):
    if N is None:
        return 0
    return N.height

# A utility function to get maximum of two integers


def max(a, b):
    if a > b:
        return a
    return b


def newNode(key):
    node = Node(key)
    node.left = None
    node.right = None
    node.height = 1  # initially added at leaf
    node.desc = 0
    return node

 # A utility function to right rotate subtree rooted with y


def rightRotate(y):
    x = y.left
    T2 = x.right
    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    # calculate the number of children of x and y
    # which are changed due to rotation.
    val = -1
    if T2 is not None:
        val = T2.desc
    y.desc = y.desc - (x.desc + 1) + (val + 1)
    x.desc = x.desc - (val + 1) + (y.desc + 1)

    return x
    # A utility function to left rotate subtree rooted with x


def leftRotate(x):
    y = x.right
    T2 = y.left
    # Perform rotation
    y.left = x
    x.right = T2
    # Update heights
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    # calculate the number of children of x and y
    # which are changed due to rotation.
    val = -1
    if T2 is not None:
        val = T2.desc
    x.desc = x.desc - (y.desc + 1) + (val + 1)
    y.desc = y.desc - (val + 1) + (x.desc + 1)

    return y
    # Get Balance factor of node N


def getBalance(N):
    if N is None:
        return 0
    return height(N.left) - height(N.right)


def insert(root, key):
    # 1. Perform the normal BST rotation
    if root is None:
        return newNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
        root.desc += 1

    elif key > root.key:
        root.right = insert(root.right, key)
        root.desc += 1

    else:  # Equal keys not allowed
        return root
    # 2. Update height of this ancestor node
    root.height = max(height(root.left), height(root.right)) + 1
# 3. Get the balance factor of this ancestor node to check whether this node became unbalanced
    balance = getBalance(root)
    # If node becomes unbalanced, 4 cases arise Left Left Case
    if balance > 1 and key < root.left.key:
        return rightRotate(root)
    # Right Right Case
    if balance < -1 and key > root.right.key:
        return leftRotate(root)
    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    # return the (unchanged) node pointer
    return root


    # Given a non-empty binary search tree, return the
# node with minimum key value found in that tree.
# Note that the entire tree does not need to be searched


def minValueNode(node):
    current = node
    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current
# Recursive function to delete a node with given key
# from subtree with given root. It returns root of
# the modified subtree.


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
        root.desc -= 1

    elif key > root.key:
        root.right = deleteNode(root.right, key)
        root.desc -= 1

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
        root.desc -= 1

    if root is None:
        return root

    root.height = max(height(root.left), height(root.right)) + 1

    balance = getBalance(root)

    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)

    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)

    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root


def preOrder(root):
    if root is not None:
        print(root.key)
        preOrder(root.left)
        preOrder(root.right)


def CountGreater(root, x):
    res = 0

    while root is not None:
        desc = -1
        if root.right is not None:
            desc = root.right.desc

        if root.key > x:
            res = res + desc + 1 + 1
            root = root.left
        elif root.key < x:
            root = root.right
        else:
            res = res + desc + 1
            break

    return res


    # Driver program to test above function
root = None
root = insert(root, 9)
root = insert(root, 5)
root = insert(root, 10)
root = insert(root, 0)
root = insert(root, 6)
root = insert(root, 11)
root = insert(root, -1)
root = insert(root, 1)
root = insert(root, 2)
# The constructed AVL Tree would be
#     9
#    / \
#     1 10
#    / \     \
#    0 5     11
#    / / \
#  -1  2  6
print("Preorder traversal of the constructed AVL tree is")
preOrder(root)

print("Number of elements greater than 9 are")
print(CountGreater(root, 9))

root = deleteNode(root, 10)

# The AVL Tree after deletion of 10
#        1
#      0 9
#     / / \
#   -1 5 11
#        / \
#        2 6

print("Preorder traversal after deletion of 10")
preOrder(root)
print('Number of elements greater than 9 are')
print(CountGreater(root, 9))


# This code is contributed by NarasingaNikhil
