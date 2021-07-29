class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
        

class Doublelinkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data,None,itr)
    
    def insert_at_beginning(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node
            
    def insertlist(self,list):
        #self.head = None # it removes the current elements in linked list
        for l in list:
            self.insert_at_end(l)
    
    
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        
        return itr.data
        
    def print_in_forward(self):
        if self.head == None:
            print('Double linked list is empty')
            return
        
        else:
            itr = self.head
            s = ''
            while itr:
                s = s + str(itr.data)+ '--->'
                itr = itr.next
                
        print(s)
        
    def print_in_backward(self):
        if self.head == None:
            print('Double linked list is empty')
            return
        
        else:
            itr = self.head   # getting lastnode
            while itr.next:
                itr = itr.next
                
            last_node = itr
            
            index = last_node
            s = ''
            while index:
                s = s + str(index.data)+ '<---'
                index = index.prev
                
        print(s)
    
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        
        return count
        
        
if __name__ == '__main__':
    d=Doublelinkedlist()
    d.insert_at_end(34)
    d.insert_at_end(23)
    d.insert_at_beginning(2)
    d.insertlist(['kalyan','sai','hi'])
    print('In forward traversal')
    d.print_in_forward()
    print('In Backward traversal')
    d.print_in_backward()
    print('Last Node')
    print(d.get_last_node())
    print('Length of linked list')
    print(d.get_length())
