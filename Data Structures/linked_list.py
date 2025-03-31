# Linked List
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        
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
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
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
    ll = LinkedList()
    ll.insert_at_beginning(1)             
    ll.insert_at_end(5)             
    ll.insert_at_end(6)             
    ll.insert_at_end(2)
    ll.print_ll()
    ll.remove_at(2)
    ll.print_ll()   
    ll.insert_at(1,79)          
    ll.print_ll()