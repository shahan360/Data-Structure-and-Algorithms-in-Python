class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def reverseList(head):
    curr = head
    prev = None
    
    while curr!=None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev      

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)

head = reverseList(head)

printList(head)   