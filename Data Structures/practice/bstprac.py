class BST:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder()
        return elements

    def preorder(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.inorder()
        if self.right:
            elements += self.right.inorder()
        return elements

    def find_max(self):
        if not self.right:
            return self.data
        return self.right.find_max()

    # def delete(self, data):


def buildBST(elements):
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    elements = [4, 2, 7, 1, 3, 6, 9]
    tree = buildBST(elements)
    print(tree.inorder())
    print(tree.preorder())
    print(tree.search(1))
    print(tree.inorder())
