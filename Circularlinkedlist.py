class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_element(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def insert_element_back(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        start = itr
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)
        
        itr.next = start
        
        
    def display(self):
        if self.head == None:
            print('Linked list is empty')
        
        i = self.head
    
        
        while i:
            print(i.data,end = ' ')
            print('--->',end = ' ')
            i=i.next
        
        
        
        print(s)
        
        

L  = Linkedlist()

L.insert_element(4)
L.insert_element(6)

L.insert_element(7)
L.insert_element_back(12)
L.display()
