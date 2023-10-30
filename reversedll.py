class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def revDLL(head):
    if head==None:
        return None
    if head.next==None:
        return head
    curr=head
    prev=None
    
    while curr!=None:
        prev=curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev
    return prev            

def printDLL(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print(curr)
    
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1

printDLL(head)

head = revDLL(head)

printDLL(head)                