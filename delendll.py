class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None
        
def deleteNode(head):
    if head==None or head.next==None:
        return None
    curr = head
    while curr.next.next!=None:
        curr = curr.next 
    curr.next = None
    return head     

def printList(head):
    curr = head
    while curr != None:
        print(curr.data,end=" ")
        curr = curr.next 
    print(head)

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)

head = deleteNode(head)

printList(head)                