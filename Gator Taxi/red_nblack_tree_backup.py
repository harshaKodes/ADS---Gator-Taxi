class RedNBlackTreeNode:
    def __init__(self, gatorride, minimum_heap_node):
        self.gatorride = gatorride
        self.parent = None  # node which the parent
        self.node_to_the_left = None  # node to the left
        self.node_to_the_right = None  # node to the right
        self.node_colour = 1  # 1 is red , 0 is black
        self.minimum_heap_node = minimum_heap_node


class RedNBlackTree:
    def __init__(self):
        self.null_node = RedNBlackTreeNode(None, None)
        self.null_node.node_to_the_left = None
        self.null_node.node_to_the_right = None
        self.null_node.node_colour = 0
        self.root = self.null_node

    # To fetch the gatorride wherein rideNumber = key
    def get_gatorride(self, key):
        temporary_variable = self.root

        # Iterate the tree to fetch node which has rideNumber = key
        while temporary_variable != self.null_node:
            if temporary_variable.gatorride.rideNumber == key:
                return temporary_variable
            if temporary_variable.gatorride.rideNumber < key:
                temporary_variable = temporary_variable.node_to_the_right
            else:
                temporary_variable = temporary_variable.node_to_the_left

        return None

    def tree_balancing_post_delete(self, node):
        
        while node != self.root and node.node_colour == 0:
            if node == node.parent.node_to_the_right:
                sibling_of_parent = node.parent.node_to_the_left
                if sibling_of_parent.node_colour != 0:
                    node.parent.node_colour = 1
                    sibling_of_parent.node_colour = 0
                    self.rotation_to_the_right(node.parent)
                    sibling_of_parent = node.parent.node_to_the_left

                if sibling_of_parent.node_to_the_right.node_colour == 0 and sibling_of_parent.node_to_the_left.node_colour == 0:
                    sibling_of_parent.node_colour = 1
                    node = node.parent
                else:
                    if sibling_of_parent.node_to_the_left.node_colour != 1:
                        sibling_of_parent.node_to_the_right.node_colour = 0
                        sibling_of_parent.node_colour = 1
                        self.rotation_to_the_left(sibling_of_parent)
                        sibling_of_parent = node.parent.node_to_the_left

                    sibling_of_parent.node_colour = node.parent.node_colour
                    node.parent.node_colour = 0
                    sibling_of_parent.node_to_the_left.node_colour = 0
                    self.rotation_to_the_right(node.parent)
                    node = self.root
            else:
                sibling_of_parent = node.parent.node_to_the_right
                if sibling_of_parent.node_colour != 0:
                    node.parent.node_colour = 1
                    sibling_of_parent.node_colour = 0
                    self.rotation_to_the_left(node.parent)
                    sibling_of_parent = node.parent.node_to_the_right

                if sibling_of_parent.node_to_the_right.node_colour == 0 and sibling_of_parent.node_to_the_left.node_colour == 0:
                    sibling_of_parent.node_colour = 1
                    node = node.parent
                else:
                    if sibling_of_parent.node_to_the_right.node_colour != 1:
                        sibling_of_parent.node_to_the_left.node_colour = 0
                        sibling_of_parent.node_colour = 1
                        self.rotation_to_the_right(sibling_of_parent)
                        sibling_of_parent = node.parent.node_to_the_right

                    sibling_of_parent.node_colour = node.parent.node_colour
                    node.parent.node_colour = 0
                    sibling_of_parent.node_to_the_right.node_colour = 0
                    self.rotation_to_the_left(node.parent)
                    node = self.root

        node.node_colour = 0

    def __rb_transplant(self, node, node_child_of_parent):
        if node.parent is None:
            self.root = node_child_of_parent
        elif node == node.parent.node_to_the_right:
            node.parent.node_to_the_right = node_child_of_parent
        else:
            node.parent.node_to_the_left = node_child_of_parent
        node_child_of_parent.parent = node.parent


    def helpingfunction_gatortaxi_node_deletion(self, node, key):
        gatortaxi_node_deletion = self.null_node
        while node != self.null_node:
            if node.gatorride.rideNumber == key:
                gatortaxi_node_deletion = node
            if node.gatorride.rideNumber >= key:
                node = node.node_to_the_left
            else:
                node = node.node_to_the_right

        if gatortaxi_node_deletion == self.null_node:
            return
        heap_node = gatortaxi_node_deletion.minimum_heap_node
        y = gatortaxi_node_deletion
        y_original_node_colour = y.node_colour
        if gatortaxi_node_deletion.node_to_the_left == self.null_node:
            x = gatortaxi_node_deletion.node_to_the_right
            self.__rb_transplant(gatortaxi_node_deletion, gatortaxi_node_deletion.node_to_the_right)
        elif (gatortaxi_node_deletion.node_to_the_right == self.null_node):
            x = gatortaxi_node_deletion.node_to_the_left
            self.__rb_transplant(gatortaxi_node_deletion, gatortaxi_node_deletion.node_to_the_left)
        else:
            y = self.minimum(gatortaxi_node_deletion.node_to_the_right)
            y_original_node_colour = y.node_colour
            x = y.node_to_the_right
            if y.parent == gatortaxi_node_deletion:
                x.parent = y
            else:
                self.__rb_transplant(y, y.node_to_the_right)
                y.node_to_the_right = gatortaxi_node_deletion.node_to_the_right
                y.node_to_the_right.parent = y

            self.__rb_transplant(gatortaxi_node_deletion, y)
            y.node_to_the_left = gatortaxi_node_deletion.node_to_the_left
            y.node_to_the_left.parent = y
            y.node_colour = gatortaxi_node_deletion.node_colour
        if y_original_node_colour == 0:
            self.tree_balancing_post_delete(x)

        return heap_node

    def tree_balancing_post_insert(self, present_node):
        while present_node.parent.node_colour == 1:
            if present_node.parent == present_node.parent.parent.node_to_the_left:
                sibling_of_parent = present_node.parent.parent.node_to_the_right

                if sibling_of_parent.node_colour == 0:
                    if present_node == present_node.parent.node_to_the_right:
                        present_node = present_node.parent
                        self.rotation_to_the_left(present_node)
                    present_node.parent.node_colour = 0
                    present_node.parent.parent.node_colour = 1
                    self.rotation_to_the_right(present_node.parent.parent)
                else:
                    sibling_of_parent.node_colour = 0
                    present_node.parent.node_colour = 0
                    present_node.parent.parent.node_colour = 1
                    present_node = present_node.parent.parent

            else:
                sibling_of_parent = present_node.parent.parent.node_to_the_left
                if sibling_of_parent.node_colour == 0:
                    if present_node == present_node.parent.node_to_the_left:
                        present_node = present_node.parent
                        self.rotation_to_the_right(present_node)
                    present_node.parent.node_colour = 0
                    present_node.parent.parent.node_colour = 1
                    self.rotation_to_the_left(present_node.parent.parent)
                else:
                    sibling_of_parent.node_colour = 0
                    present_node.parent.node_colour = 0
                    present_node.parent.parent.node_colour = 1
                    present_node = present_node.parent.parent

            if present_node == self.root:
                break
        self.root.node_colour = 0

    def fetch_gatorrides_in_range(self, node, begin, end, gatortaxi_output):
        if node == self.null_node:
            return

        if begin < node.gatorride.rideNumber:
            self.fetch_gatorrides_in_range(node.node_to_the_left, begin, end, gatortaxi_output)
        if begin <= node.gatorride.rideNumber <= end:
            gatortaxi_output.append(node.gatorride)
        self.fetch_gatorrides_in_range(node.node_to_the_right, begin, end, gatortaxi_output)

    def get_gatorrides_in_range(self, begin, end):
        gatortaxi_output = []
        self.fetch_gatorrides_in_range(self.root, begin, end, gatortaxi_output)
        return gatortaxi_output

    def minimum(self, node):
        while node.node_to_the_left != self.null_node:
            node = node.node_to_the_left
        return node

    def rotation_to_the_left(self, x):
        y = x.node_to_the_right
        x.node_to_the_right = y.node_to_the_left
        if y.node_to_the_left != self.null_node:
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
        if y.node_to_the_right != self.null_node:
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

    def insert(self, gatorride, heap_minimum):
        node = RedNBlackTreeNode(gatorride, heap_minimum)
        node.parent = None
        node.node_to_the_left = self.null_node
        node.node_to_the_right = self.null_node
        node.node_colour = 1

        node_to_be_inserted = None
        node_temporary = self.root

        while node_temporary != self.null_node:
            node_to_be_inserted = node_temporary
            if node.gatorride.rideNumber < node_temporary.gatorride.rideNumber:
                node_temporary = node_temporary.node_to_the_left
            else:
                node_temporary = node_temporary.node_to_the_right

        node.parent = node_to_be_inserted
        if node_to_be_inserted is None:
            self.root = node
        elif node.gatorride.rideNumber > node_to_be_inserted.gatorride.rideNumber:
            node_to_be_inserted.node_to_the_right = node
        else:
            node_to_be_inserted.node_to_the_left = node

        if node.parent is None:
            node.node_colour = 0
            return

        if node.parent.parent is None:
            return

        self.tree_balancing_post_insert(node)

    def gatortaxi_node_deletion(self, rideNumber):
        return self.helpingfunction_gatortaxi_node_deletion(self.root, rideNumber)
