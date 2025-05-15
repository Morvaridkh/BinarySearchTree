class Node:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.left = None
        self.right = None
        self.parent = None

    def _get_edges(self):
        return [self.left, self.right]


class BSTtree:
    def __init__(self):
        self.root = None
        self.count_node = 0

    def insert(self, ID, name):
        """
        Inserts a new node with the given ID and name into the BST.
        Args:
        - ID: The ID of the new node.
        - name: The name of the new node.
        """
        # Create a new node
        new_node = Node(ID, name)
        # Track the node's parent while traversing
        parent = None
        current = self.root
        # Traverse the tree to find the correct insertion point
        while current is not None:
            parent = current
            if new_node.ID < current.ID:
                current = current.left
            else:
                current = current.right
        # Set the parent of the new node
        new_node.parent = parent
        # If the tree is empty, set the new node as the root
        if parent is None:
            self.root = new_node
        # Insert the new node as the left or right child
        elif new_node.ID < parent.ID:
            parent.left = new_node
        else:
            parent.right = new_node
        # Increase the node count
        self.count_node += 1

    def search(self, current_node, ID):
        """
        Searches for a node by its ID in the BST.
        Args:
        - current_node: The node to start searching from.
        - ID: The ID of the node to search for.

        Returns:
        - The node if found, or None if not found.
        """
        # Base case: node is found or we've reached the end of the tree
        if current_node is None or current_node.ID == ID:
            return current_node

        # If the ID is smaller, search in the left subtree
        if ID < current_node.ID:
            return self.search(current_node.left, ID)
        # If the ID is larger, search in the right subtree
        else:
            return self.search(current_node.right, ID)
    def sizeBST(self):
        return self.count_node

    def preorder(self, node):
        """
        Performs a preorder traversal of the tree and prints each node's ID and name.
        Args:
        - node: The node to start the traversal from.
        """
        if node:
            # Print the current node's data
            print(f"ID: {node.ID}, Name: {node.name}")
            # Recursively traverse the left and right subtrees
            self.preorder(node.left)
            self.preorder(node.right)

    def _get_edges(self):
        edges = [self.root._get_edges()]
        if self.root.left is not None:
            edges.append(self.root.left._get_edges())
        if self.root.right is not None:
            edges.append(self.root.right._get_edges())
        return edges

bst = BSTtree()

bst.insert(1, "Node A")
bst.insert(6, "Node B")
bst.insert(4, "Node C")
bst.insert(12, "Node D")
bst.insert(90, "Node E")
bst.insert(54, "Node F")


bst.preorder(bst.root)

result = bst.search(bst.root, 4)
if result:
    print(f"Found: ID={result.ID}, Name={result.name}")
else:
    print("Node not found.")

print(f"Total nodes in the BST: {bst.sizeBST()}")

