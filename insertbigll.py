class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insertBLL(head,data):
    temp = Node(data)
    temp.next = head
    return temp

head = None
head = insertBLL(head,10) 
head = insertBLL(head,20)  
head = insertBLL(head,30)
head = insertBLL(head,40)  

def printList(head):
    curr = head
    while curr!=None:
        print(curr.data,end=" ")
        curr = curr.next 
        
printList(head)           