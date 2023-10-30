from dataclasses import dataclass


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insertEnd(head,data):
    if head==None:
        return Node(data)
    curr = head
    while curr.next!=None:
        curr = curr.next 
    curr.next = Node(data)
    return head     

head  = None
head  = insertEnd(head,10)
head  = insertEnd(head,20)
head  = insertEnd(head,30)

def printList(head):
    curr = head
    while curr!=None:
        print(curr.data,end=" ")
        curr = curr.next
        
printList(head)                