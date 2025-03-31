# Linked List
class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        if self.head is None:
            node = Node(data,self.head,None)
            self.head = node
        else:
            node = Node(data,self,None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None,itr)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        return count
    
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            print("Invalid Index")
            return
        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count+=1
    
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
    
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1        
    
    def print_backward(self):
        if self.head is None:
            print("Empty Linked List")
            return
        s = ''
        itr = self.head
        while itr.next:
            itr = itr.next
        
        while itr:
            s += str(itr.data) + '-->'
            itr = itr.prev
        print(s)
    
    def print_ll(self):
        if self.head is None:
            print("Empty Linked List")
            return
        s = ''
        itr = self.head
        while itr:
            s += str(itr.data)+'-->'
            itr = itr.next
        print(s)




if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_beginning(1)
    dll.insert_at_end(4)
    dll.insert_at_end(3)
    dll.insert_at_end(9)
    dll.insert_at_end(6)
    dll.print_ll()
    dll.remove_at(2)
    dll.print_ll()
    dll.print_backward()