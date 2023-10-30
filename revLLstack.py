class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def reverseList(head):
    stack = []
    curr = head
    while curr!=None:
        stack.append(curr.data)
        curr=curr.next 
    curr = head 
    while curr!=None:
        curr.data = stack.pop()
        curr=curr.next
    return head         

def printLL(head):
    curr = head
    while curr!=None:
        print(curr.data,end=" ")
        curr = curr.next 
    print(head)

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printLL(head)

head = reverseList(head)

printLL(head)
                