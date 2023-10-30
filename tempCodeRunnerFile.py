def insertBig(head,x): #O(n) time complexity
    temp=Node(x)
    if head==None:
        temp.next=temp 
        return temp
    curr = head
    while curr.next!=head:
        curr=curr.next 
    
    curr.next = temp
    temp.next = head
    return head 