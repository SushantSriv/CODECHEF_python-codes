class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:

    def __init__(self):
        self.head=None
        
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def delete(self,count):
        count1=1
        temp=self.head

        if(temp is not None):
            if(count1==count):
                self.head=temp.next
                temp=None
                return
        while(temp is not None):
            if count1==count:
                break
            else:
                count1+=1
            prev=temp
            temp=temp.next
        if(temp is None):
            return
        prev.next=temp.next
        temp=None

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next


    def push(self,newdata):
        
        new_node=node(newdata)
        new_node.next=self.head
        self.head=new_node


    def insertaf(self,prev_node,newdata):

       if prev_node is None:
            print("list is null")
            return
       new_node=node(newdata) 
       new_node.next=prev_node.next
       prev_node.next=new_node

    def append(self,newdata):

        new_node=node(newdata)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node

    def countllist(self):
        temp=self.head
        count=1
        while(temp):
            temp=temp.next
            count+=1
        print(count)

    def searchiter(self,key):
        m=0
        temp=self.head
        if(temp is not None):
            if(temp.data==key):
                print("True")
                m=1
                return
                
        while(temp is not None):
            if(temp.data==key):
                print("True")
                m=1
                break
            else:
                temp=temp.next 
        if(m==0):
            print("False")
    def swapNodes(self, x, y):
 
        # Nothing to do if x and y are same
        if x == y:
            return
 
        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
 
        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
 
        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else: #make y the new head
            self.head = currY
 
        # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else: # make x the new head
            self.head = currX
 
        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

        
    def findn(self,n):
        curr=self.head
        for i in range(n-1):
            curr=curr.next
        print(curr.data)
        
    def mid(self):
        temp=self.head
        count=0
        while(temp is not None):
            temp=temp.next
            count+=1
        print(count)    
        temp=self.head    
        for i in range((count-1)//2):
            temp=temp.next
        print(temp.data)
    def findnlast(self,n):
        temp=self.head
        count=0
        while(temp is not None):
            temp=temp.next
            count+=1
        temp=self.head
        for i in range(count-n):
            temp=temp.next
        print(temp.data)

    def dellist(self):
        prev=None
        temp=self.head
        while(temp is not None):
            prev=temp.next
            del temp.data
            temp=prev
        print("List Deleted")     
            
    def countint(self,key):
        temp=self.head
        count=0
        while(temp):
            if temp.data==key:
                count+=1
                temp=temp.next
            else:
                temp=temp.next
        print(count)

    def movefrontend(self):
        slast=None
        last=self.head
        while(last.next):
            slast=last
            last=last.next
        slast.next=None
        last.next=self.head
        self.head=last
        

                
            
                  
if __name__=="__main__":
    
    llist=Linkedlist()
    llist.head=node(1)
    llist.push(2)
    llist.push(30)
    llist.push(40)
    llist.print()
    print("|||||||||||||||||||")
    llist.print()
    print("|||||||||||||||||||||")
    llist.countllist()
    llist.push(8)
    llist.push(2)
    llist.push(76)
    llist.print()
    print("||||||||||||||||||||||||||||||")
    llist.countllist()
    llist.countllist()
    llist.searchiter(8)
    llist.searchiter(12)
    llist.print()
    llist.swapNodes(2,30)
    print("|||||||||||||||||||")
    llist.print()
    print("||||||||||||||||||||||")
    llist.mid()
    llist.findnlast(6)
    llist.countint(40)
    print("||||||||||||||||||||")
    llist.print()
    print("||||||||||||||||||||")
    llist.movefrontend()
    llist.print()

            
        
