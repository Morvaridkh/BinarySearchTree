class Node:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.left = None
        self.right = None
        self.parent = None

class BSTtree:
    def __init__(self):
        self.root = None
        self.count_node = 0

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
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.ID < parent.ID:
            parent.left = new_node
        else:
            parent.right = new_node
        self.count_node += 1

    def search(self, ID):
        #Searches for a node by its ID in the BST.
        def _search(current_node, ID):
            if current_node is None or current_node.ID == ID:
                return current_node
            if ID < current_node.ID:
                return _search(current_node.left, ID)
            else:
                return _search(current_node.right, ID)
        return _search(self.root, ID)

    def transplant(self, node_to_replace, new_node):
        #Replaces the subtree rooted at node_to_replace with new_node.
        if node_to_replace.parent is None:
            self.root = new_node
        elif node_to_replace == node_to_replace.parent.left:
            node_to_replace.parent.left = new_node
        else:
            node_to_replace.parent.right = new_node
        if new_node is not None:
            new_node.parent = node_to_replace.parent

    def find_minimum(self, node):
        #Finds the node with the minimum ID in the subtree rooted at node.
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, node_to_delete):
        if node_to_delete is None:
            return
        self.count_node -= 1
        if node_to_delete.left is None:
            self.transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is None:
            self.transplant(node_to_delete, node_to_delete.left)
        else:
            successor = self.find_minimum(node_to_delete.right)
            if successor.parent != node_to_delete:
                self.transplant(successor, successor.right)
                successor.right = node_to_delete.right
                successor.right.parent = successor
            self.transplant(node_to_delete, successor)
            successor.left = node_to_delete.left
            successor.left.parent = successor

    def preorder(self, node):
        if node:
            print(f"ID: {node.ID}, Name: {node.name}")
            self.preorder(node.left)
            self.preorder(node.right)

    def sizeBST(self):
        return self.count_node

bst = BSTtree()

# Insert nodes (same as your original test)
bst.insert(1, "Node A")
bst.insert(6, "Node B")
bst.insert(4, "Node C")
bst.insert(12, "Node D")
bst.insert(90, "Node E")
bst.insert(54, "Node F")

# Print tree before deletion
print("Before:")
bst.preorder(bst.root)


node_to_delete = bst.search(6)
if node_to_delete:
    bst.delete_node(node_to_delete)
    print("\nAfter deleting node:")
    bst.preorder(bst.root)
    print(f"Total nodes: {bst.sizeBST()}")
else:
    print("Node to delete not found.")

# Verify the tree structure
print("\nRoot:", bst.root.ID if bst.root else "None")
print("Root's left:", bst.root.left.ID if bst.root and bst.root.left else "None")
print("Root's right:", bst.root.right.ID if bst.root and bst.root.right else "None")