


class MyBinarySearchTree:

    class Node:
        def __init__(self, element, left, right):
            self.element = element
            self.left = left
            self.right = right

        def __repr__(self):
            return repr(self.element)

    def __init__(self):
        self.root = None
        self.size = 0


    def _find_rec(self, node, element):
        """
        Starting at the subtree rooted in node, find the node object that
        contains the element. If it doesn't exist, return None.
        """
        if node == None:
            return None
        
        # node is not None
        if node.element > element: # node must be in the left subtree:
            return self._find_rec(node.left, element) ## need element here because we gotta
            ## still look for the element
        elif node.element < element: # node in question must be in the right subtree
            return self._find_rec(node.right, element)
        else: ## element must be current node.element
            return node

    def find(self, element):
        node = self._find_rec(self.root, element)
        if node == None:
            return None
        else:
            return node#.element?
            #why would we return the element here? we obviously already know the element if
            # could put that argument into the function. so what we'd really want to return
            # is the node object containing the element, no??

    def _insert_rec(self, node, element):
        """
        Starting at the subtree rooted in node, find the node object that contains the element
        if it doesn't exist, create a new node there.
        """

        # base case: 
        # we are exactly where we need to be and we create a new node with the element
        # = element
        if node is None:
            return self.Node(element, None, None)
        
        if node.element > element: # node must be in the left subtree
            node.left = self._insert_rec(node.left, element)
        elif node.element < element: # node must be in the right subtree
            node.right = self._insert_rec(node.right, element)
        
        return node ## we return node because when we get to a place where say right
        ## child is None, then we to a function call on that, get nonde so make a new node
        ## and return that new node from the function call, so now we have like the previous
        ## node.right = to our new node as well

    def insert(self, element):
        self.root = self._insert_rec(self.root, element)
        self.size += 1

    def _inorder(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        if node is None:
            return [] # this is how we will statr the list
        # need to do this for each node in the left subtree, the current node, and
        # then the right subtree
        return self._inorder_rec(node.left) + [node.element] + self._inorder_rec(node.right)

    def __iter__(self):
        return iter(self._inorder)

    def __len__(self):
        return self.size

if __name__ == "__main__":
    bst = MyBinarySearchTree()
    bst.insert("A")
    bst.insert("B")
    bst.insert("C")
    bst.insert("D")
    

    print(bst.find("D"))


