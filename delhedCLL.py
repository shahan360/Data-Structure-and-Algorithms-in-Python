class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# def delHead(head): #O(n) time complexity
#     if head==None:
#         return None
#     elif head.next==head:
#         return None 
#     else:
#         curr = head
#         while curr.next!=head:
#             curr=curr.next 
#         curr.next=head.next 
#         return curr.next  

def delHead(head): #O(1) time complexity
    if head==None:
        return None
    elif head.next==head:
        return None 
    else:
        head.data = head.next.data
        head.next = head.next.next 
        
        return head    

def printCircular(head):
    if head==None:
        return None
    print(head.data,end=" ")
    curr = head.next 
    while curr!=head:
        print(curr.data,end=" ")
        curr=curr.next 
    print(curr)    

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

printCircular(head)

head = delHead(head)

printCircular(head)     