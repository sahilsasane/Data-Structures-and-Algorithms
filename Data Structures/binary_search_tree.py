class BSTnode:
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
                self.left = BSTnode(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTnode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
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
            elements += self.left.preorder()

        if self.right:
            elements += self.right.preorder()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            max_val = self.left.find_max()
            min_val = self.right.find_min()
            # self.data = min_val
            self.data = max_val
            # self.right = self.right.delete(min_val)
            self.left = self.left.delete(max_val)
        return self


def buildBST(elements):
    root = BSTnode(elements[0])

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
