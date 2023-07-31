import sys

class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None  #parent node
        self.node_to_the_left = None   # node to the left
        self.node_to_the_right = None  # node to the right
        self.node_colour = 1     # 1 is red , 0 is black


class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.node_colour = 0
        self.TNULL.node_to_the_left = None
        self.TNULL.node_to_the_right = None
        self.root = self.TNULL

    def helping_for_preorder(self, node):
        if node != TNULL:
            sys.stdout.write(node.item + " ")
            self.helping_for_preorder(node.node_to_the_left)
            self.helping_for_preorder(node.node_to_the_right)

    # tree balancing post deletion
    def fixing_deletion(self, x):
        while x != self.root and x.node_colour == 0:
            if x == x.parent.node_to_the_left:
                s = x.parent.node_to_the_right
                if s.node_colour == 1:
                    s.node_colour = 0
                    x.parent.node_colour = 1
                    self.rotation_to_the_left(x.parent)
                    s = x.parent.node_to_the_right

                if s.node_to_the_left.node_colour == 0 and s.node_to_the_right.node_colour == 0:
                    s.node_colour = 1
                    x = x.parent
                else:
                    if s.node_to_the_right.node_colour == 0:
                        s.node_to_the_left.node_colour = 0
                        s.node_colour = 1
                        self.rotation_to_the_right(s)
                        s = x.parent.node_to_the_right

                    s.node_colour = x.parent.node_colour
                    x.parent.node_colour = 0
                    s.node_to_the_right.node_colour = 0
                    self.rotation_to_the_left(x.parent)
                    x = self.root
            else:
                s = x.parent.node_to_the_left
                if s.node_colour == 1:
                    s.node_colour = 0
                    x.parent.node_colour = 1
                    self.rotation_to_the_right(x.parent)
                    s = x.parent.node_to_the_left

                if s.node_to_the_right.node_colour == 0 and s.node_to_the_right.node_colour == 0:
                    s.node_colour = 1
                    x = x.parent
                else:
                    if s.node_to_the_left.node_colour == 0:
                        s.node_to_the_right.node_colour = 0
                        s.node_colour = 1
                        self.rotation_to_the_left(s)
                        s = x.parent.node_to_the_left

                    s.node_colour = x.parent.node_colour
                    x.parent.node_colour = 0
                    s.node_to_the_left.node_colour = 0
                    self.rotation_to_the_right(x.parent)
                    x = self.root
        x.node_colour = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.node_to_the_left:
            u.parent.node_to_the_left = v
        else:
            u.parent.node_to_the_right = v
        v.parent = u.parent

    def help_node_deletion(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.node_to_the_right
            else:
                node = node.node_to_the_left

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_node_colour = y.node_colour
        if z.node_to_the_left == self.TNULL:
            x = z.node_to_the_right
            self.__rb_transplant(z, z.node_to_the_right)
        elif (z.node_to_the_right == self.TNULL):
            x = z.node_to_the_left
            self.__rb_transplant(z, z.node_to_the_left)
        else:
            y = self.minimum(z.node_to_the_right)
            y_original_node_colour = y.node_colour
            x = y.node_to_the_right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.node_to_the_right)
                y.node_to_the_right = z.node_to_the_right
                y.node_to_the_right.parent = y

            self.__rb_transplant(z, y)
            y.node_to_the_left = z.node_to_the_left
            y.node_to_the_left.parent = y
            y.node_colour = z.node_colour
        if y_original_node_colour == 0:
            self.fixing_deletion(x)

    # Balancing tree post insertion
    def fixing_insertion(self, k):
        while k.parent.node_colour == 1:
            if k.parent == k.parent.parent.node_to_the_right:
                u = k.parent.parent.node_to_the_left
                if u.node_colour == 1:
                    u.node_colour = 0
                    k.parent.node_colour = 0
                    k.parent.parent.node_colour = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.node_to_the_left:
                        k = k.parent
                        self.rotation_to_the_right(k)
                    k.parent.node_colour = 0
                    k.parent.parent.node_colour = 1
                    self.rotation_to_the_left(k.parent.parent)
            else:
                u = k.parent.parent.node_to_the_right

                if u.node_colour == 1:
                    u.node_colour = 0
                    k.parent.node_colour = 0
                    k.parent.parent.node_colour = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.node_to_the_right:
                        k = k.parent
                        self.rotation_to_the_left(k)
                    k.parent.node_colour = 0
                    k.parent.parent.node_colour = 1
                    self.rotation_to_the_right(k.parent.parent)
            if k == self.root:
                break
        self.root.node_colour = 0

    # Printing function
    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_node_colour = "RED" if node.node_colour == 1 else "BLACK"
            print(str(node.item) + "(" + s_node_colour + ")")
            self.__print_helper(node.node_to_the_left, indent, False)
            self.__print_helper(node.node_to_the_right, indent, True)

    def preorder(self):
        self.helping_for_preorder(self.root)

    def minimum(self, node):
        while node.node_to_the_left != self.TNULL:
            node = node.node_to_the_left
        return node

    def maximum(self, node):
        while node.node_to_the_right != self.TNULL:
            node = node.node_to_the_right
        return node

    def successor(self, x):
        if x.node_to_the_right != self.TNULL:
            return self.minimum(x.node_to_the_right)

        y = x.parent
        while y != self.TNULL and x == y.node_to_the_right:
            x = y
            y = y.parent
        return y

    def predecessor(self,  x):
        if (x.node_to_the_left != self.TNULL):
            return self.maximum(x.node_to_the_left)

        y = x.parent
        while y != self.TNULL and x == y.node_to_the_left:
            x = y
            y = y.parent

        return y

    def rotation_to_the_left(self, x):
        y = x.node_to_the_right
        x.node_to_the_right = y.node_to_the_left
        if y.node_to_the_left != self.TNULL:
            y.node_to_the_left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.node_to_the_left:
            x.parent.node_to_the_left = y
        else:
            x.parent.node_to_the_right = y
        y.node_to_the_left = x
        x.parent = y

    def rotation_to_the_right(self, x):
        y = x.node_to_the_left
        x.node_to_the_left = y.node_to_the_right
        if y.node_to_the_right != self.TNULL:
            y.node_to_the_right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.node_to_the_right:
            x.parent.node_to_the_right = y
        else:
            x.parent.node_to_the_left = y
        y.node_to_the_right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.node_to_the_left = self.TNULL
        node.node_to_the_right = self.TNULL
        node.node_colour = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.node_to_the_left
            else:
                x = x.node_to_the_right

        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.node_to_the_left = node
        else:
            y.node_to_the_right = node

        if node.parent == None:
            node.node_colour = 0
            return

        if node.parent.parent == None:
            return

        self.fixing_insertion(node)

    def get_root(self):
        return self.root

    def delete_node(self, item):
        self.help_node_deletion(self.root, item)

    def print_tree(self):
        self.__print_helper(self.root, "", True)


if __name__ == "__main__":
    bst = RedBlackTree()

    bst.insert(70)
    bst.insert(60)
    bst.insert(85)
    bst.insert(80)
    bst.insert(95)
    bst.insert(65)

    bst.print_tree()
    print("\nAfter deleting an element")
    bst.delete_node(80)
    bst.print_tree()