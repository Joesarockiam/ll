class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def ins_beg(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp
    def ins_end(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=temp
    def ins_pos(self,data,position):
        count=1
        curr=self.head
        while count<position-1 and curr!=None:
            curr=curr.next
            count+=1
        temp=Node(data)
        temp.next=curr.next
        curr.next=temp
    def del_beg(self):
            if self.head==None:
                print("Empty Linked List")
            else:
                temp=self.head
                self.head=self.head.next
                del temp
    def del_end(self):
            if self.head==None:
                print("Empty Linked List")
            else:
                curr=self.head
                prev=None
                while curr.next!=None:
                    prev=curr
                    curr=curr.next
                prev.next=curr.next
                del curr
    def del_pos(self,position):
            if self.head==None:
                print("Empty Linked List")
            else:
                curr=self.head
                prev=None
                count=1
                while curr!=None and count<position:
                    prev=curr
                    curr=curr.next
                    count+=1
                prev.next=curr.next
                del curr
    def search(self,p_id):
        curr=self.head
        while curr!=None:
            if(curr.data[0]==p_id):
                print(curr.data)
                break
            curr=curr.next
    def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next
ll=linkedList()
while True:
    print("Press 1 for to insert\nPress 2 to delete\nPress 3 to update\nPress 4 to search and print the product details\nPress 5 to traverse")
    ch=int(input("Enter your choice:"))
    if ch==1:
            print("Press 1 to insert at the beginning\nPress 2 to insert at any position\nPress 3 to insert at the end")
            c=int(input("Enter 1/2/3:"))
            p_id=input("Enter product id:")
            p_name=input("Enter name:")
            p_price=float(input("Enter price:"))
            if(c==1):
                ll.ins_beg([p_id,p_name,p_price])
            elif(c==2):
                pos=int(input("Enter position to insert:"))
                ll.ins_pos([p_id,p_name,p_price],pos)
            elif(c==3):
                ll.ins_end([p_id,p_name,p_price])
    elif(ch==2):
        print("Press 1 to delete at the beginning\nPress 2 to delete at any position\nPress 3 to delete at the end")
        c=int(input("Enter 1/2/3:"))
        if(c==1):
            ll.del_beg()
        elif(c==2):
            pos=int(input("Enter position to insert:"))
            ll.del_pos(pos)
        elif(c==3):
            ll.del_end()
    elif(ch==3):
        ll.traverse()
        pos=int(input("Enter the node to be updated:"))
        ll.del_pos(pos)
        p_id=int(input("Enter the product id:"))
        p_name=input("Enter name:")
        p_price=float(input("Enter price:"))
        ll.ins_pos([p_id,p_name,p_price],pos)
    elif(ch==4):
        p_id=input("Enter product id to search:")
        ll.search(p_id)
    elif ch==5:
        ll.traverse()
    else:
        break
