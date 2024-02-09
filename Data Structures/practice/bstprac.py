class BST:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def search(self, data):
        if self.data == data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        elif data > self.data:
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

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        return self


def buildBST(elements):
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    elements = [4, 2, 7, 1, 3, 6, 9]
    tree = buildBST(elements)
    print(tree.inorder())
    # print(tree.preorder())
    print(tree.search(1))
    tree.delete(3)
    print(tree.inorder())
