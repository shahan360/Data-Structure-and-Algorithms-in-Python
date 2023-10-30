class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# def insertBig(head,x): #O(n) time complexity
#     temp=Node(x)
#     if head==None:
#         temp.next=temp 
#         return temp
#     curr = head
#     while curr.next!=head:
#         curr=curr.next 
    
#     curr.next = temp
#     temp.next = head
#     return head      

def insertBig(head,x): #O(1) time complexity
    temp = Node(x)
    if head==None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next 
        head.next = temp 
        head.data,temp.data=temp.data,head.data #swapping node data
    return temp 

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

head = insertBig(head,5)

printCircular(head)  