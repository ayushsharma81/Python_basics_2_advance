# Python 3 implementation for Top-Down
# Red-Black Tree Insertion creating
# a red black tree and storing an
# English sentence into it using Top
# down insertion approach

# Class for performing
# RBTree operations
class RbTree:

    Root = None

    # Function to calculate
    # the height of the tree
    def HeightT(self,Root):

        lefth, righth=0, 0

        if (Root == None or (Root.children == None and Root.children[1] == None)):
            return 0
        lefth = self.HeightT(Root.children[0])
        righth = self.HeightT(Root.children[1])

        return (max(lefth, righth) + 1)

    # Function to check if
    # dir is equal to 0
    @staticmethod
    def check(dir):
        return 1 if dir == 0 else 0

    # Function to check if a
    # node's color is red or not
    @staticmethod
    def isRed(Node):
        return Node != None and Node.color=="R"

    # Function to perform
    # single rotation
    def SingleRotate(self, Node, dir):

        temp = Node.children[self.check(dir)]
        Node.children[self.check(dir)] = temp.children[dir]
        temp.children[dir] = Node
        self.Root.color = "R"
        temp.color = "B"

        return temp

    # Function to perform double rotation
    def DoubleRotate(self, Node, dir):

        Node.children[self.check(dir)] = self.SingleRotate(Node.children[self.check(dir)], self.check(dir))
        return self.SingleRotate(Node, dir)

    # Function to insert a new
    # node with given data
    def Insert(self, tree, data):

        if (tree.Root == None):

            tree.Root = TreeNode(data)
            if (tree.Root == None):
                return None
        else:

            # A temporary root
            temp = TreeNode("")

            # Grandparent and Parent
            g, t=None,None
            p, q=None,None

            dir = 0; last = 0

            t = temp

            g = p = None

            t.children[1] = tree.Root

            q = t.children[1]
            while (True):

                if (q == None):

                    # Inserting root node
                    q = TreeNode(data)
                    p.children[dir] = q

                # Sibling is red
                elif (self.isRed(q.children[0]) and self.isRed(q.children[1])):

                    # Recoloring if both
                    # children are red
                    q.color = "R"
                    q.children[0].color = "B"
                    q.children[1].color = "B"

                if (self.isRed(q) and self.isRed(p)):

                    # Resolving red-red
                    # violation
                    dir2=0
                    if (t.children[1] == g):
                        dir2 = 1
                    else:
                        dir2 = 0

                    # If children and parent
                    # are left-left or
                    # right-right of grand-parent
                    if (q == p.children[last]):
                        t.children[dir2] = self.SingleRotate(g, 1 if last == 0 else 0)

                    # If they are opposite
                    # childs i.e left-right
                    # or right-left
                    else:
                        t.children[dir2] = self.DoubleRotate(g,1 if last == 0 else 0)

                # Checking for correct
                # position of node
                if (q.data==data):
                    break
                last = dir

                # Finding the path to
                # traverse [Either left
                # or right ]
                dir = 1 if q.data<data else 0

                if (g != None):
                    t = g

                # Rearranging pointers
                g = p
                p = q
                q = q.children[dir]

            tree.Root = temp.children[1]

        # Assign black color
        # to the root node
        tree.Root.color = "B"

        return tree.Root

    # Print nodes at each
    # level in level order
    # traversal
    def PrintLevel(self, root, i):
        if (root == None):
            return

        if (i == 1):
            print("| {} | {} |".format(root.data,root.color),end='')

            if (root.children[0] != None): 
                print(" {} |".format(root.children[0].data),end='')
            else:
                print(" None |",end='')
            if (root.children[1] != None):
                print(" {} |".format(root.children[1].data),end='')
            else:
                print(" None |",end='')

            return

        self.PrintLevel(root.children[0], i - 1)
        self.PrintLevel(root.children[1], i - 1)

    # Utility Function to perform 
    # level order traversal
    def LevelOrder(self, root):

        for i in range(self.HeightT(root) + 1):
            self.PrintLevel(root, i)
            print('\n')

# Class for representing
# a node of the tree
class TreeNode: 
    def __init__(self, data):

        # Color R- Red
        # and B - Black
        self.data = data
        self.color = "R"
        self.children = [None,None]

# Driver Code
if __name__=='__main__':
    # Tree Node Representation
    # -------------------------------------------
    # DATA | COLOR | LEFT CHILD | RIGHT CHILD |
    # -------------------------------------------
    Tree = RbTree()
    Sentence, Word='',''
    Sentence = "old is gold"
    Word_Array = Sentence.split()

    for i in range(len(Word_Array)):
        Tree.Root = Tree.Insert(Tree, Word_Array[i])

    # Print Level Order Traversal
    print("The Level Order Traversal the tree is:")
    Tree.LevelOrder(Tree.Root)
    print("\nInserting a word in the tree:")
    Word = "forever"
    Tree.Root = Tree.Insert(Tree, Word)

    Tree.LevelOrder(Tree.Root)
# This code is contributed by Amartya Ghosh
