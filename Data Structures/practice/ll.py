class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def printll(self):
        if self.head is None:
            print("Empty Linked list")
            return
        s = ""
        itr = self.head
        while itr:
            s += str(itr.data) + "-->"
            itr = itr.next
        print(s)

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise ("invalid index")
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise ("invalid index")

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


ll = LinkedList()
ll.insert_beginning(4)
ll.insert_beginning(3)
ll.insert_beginning(2)
ll.printll()
ll.insert_end(9)
ll.printll()
ll.insert_at(2, 110)
ll.printll()
ll.remove_at(3)
ll.printll()
