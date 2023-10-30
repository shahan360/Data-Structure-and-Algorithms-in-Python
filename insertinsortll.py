class Node:
    def __init__(self,data) :
        self.data  = data
        self.next = None 

def sortedInsert(head,x):
      temp = Node(x)
      
      if head==None:
          return temp
      elif x<head.data:
          temp.next=head
          return temp
      else:
          curr = head
          while curr.next!=None and curr.next.data<x:
              curr=curr.next 
          temp.next = curr.next
          curr.next = temp
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

head = sortedInsert(head, 35)

printLL(head)              