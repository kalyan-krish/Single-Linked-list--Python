class Node: # Node class
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class Linkedlist: #Linked list class
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):#insert at beginning 
        node = Node(data,self.head)
        self.head=node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        s = ''
        
        while itr:
            s += str(itr.data) + '--->'
            itr = itr.next
        
        print(s)
        
    def insert_at_end(self,data):#insert at end
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)
        
    def insert_list(self,list):#insert the list elements 
        self.head = None
        for data in list:
            self.insert_at_end(data)
    
    def get_length(self): # linked list length
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def remove_ele_at(self,index): # removing element at index
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1
            
    #Insert element at specific index        
    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        if index == self.get_length() - 1:
            self.insert_at_end(data)
            return
        
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
            
            itr = itr.next
            count += 1
        
         

if __name__ == "__main__":
    ll = Linkedlist()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(1)
    ll.insert_at_end(3)
    m = ['k','a','l','y','a','n'] 
    ll.insert_list(m)# creating linked list for this list
    print(ll.get_length())# length of linked list
    ll.remove_ele_at(2) # removing element at that index
    #ll.remove_ele_at(8) # raised exception of index
    ll.insert_at(3,'m')
  
    ll.print()
        
