class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val)
                return self.preorder_search(start.right,find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start is not None:
            traversal = traversal + str(start.value) + "->"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def insert(self, new_val):
        
        pass

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)

if __name__ == '__main__':

# Set up tree
    tree = BST(4)

# Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

# Check search
# Should be True
    print (tree.search(4))
# Should be False
    print (tree.search(6))