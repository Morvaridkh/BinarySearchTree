class Node:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.parent = None
        self.right = None
        self.left = None

    def is_left(self):
        if self.parent is None:
            return False
        return self == self.parent.left

    def is_right(self):
        if self.parent is None:
            return False
        return self == self.parent.right

    def __str__(self):
        return f"Node(ID={self.ID}, name=<{self.name}>)"


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        # we don't have root!
        return self.root is None

    def insert(self, ID, name):
        #Inserts a new node with the given ID and name into the BST.
        new_node = Node(ID, name)
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if new_node.ID < current.ID:
                current = current.left
            else:
                current = current.right
        # new node is child of parent
        new_node.parent = parent
        # tree is empty and you insert a new node
        if parent is None:
            self.root = new_node
        elif new_node.ID < parent.ID:
            parent.left = new_node
        else:
            parent.right = new_node
        return new_node

    def search(self, ID, current_node=None):
        # if tree is empty return nothing
        if self.is_empty(): return
        # start searching from the root
        if current_node is None:
            current_node = self.root
        if ID < current_node.ID:
            return self.search(ID, current_node.left)
        elif ID > current_node.ID:
            return self.search(ID, current_node.right)
        else:
            return current_node

    def transplant(self, old_node, new_node):
        #Replaces the subtree rooted at old_node with new_node.
        if old_node.parent is None:
            self.root = new_node
        elif old_node == old_node.parent.left:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node
        if new_node is not None:
            new_node.parent = old_node.parent

    def find_minimum(self, node=None):
        if node is None:
            node = self.root
        #Finds the node with the minimum ID in the subtree rooted at node.
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            successor = self.find_minimum(node.right)
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def print(self, node=None):
        if node is None:
            node = self.root

        if node is not None:
            print(node)
            if node.left is not None:
                self.print(node.left)
            if node.right is not None:
                self.print(node.right)

    def size(self, node=None):
        if self.root is None:
            return 0

        # start counting from the root
        if node is None:
            node = self.root

        counter = 0
        if node is not None:
            counter += 1
            if node.left is not None:
                counter += self.size(node.left)
            if node.right is not None:
                counter += self.size(node.right)

        return counter
