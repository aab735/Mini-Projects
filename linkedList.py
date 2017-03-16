class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext

#temp = Node(93)
#print temp.getData()

class unorderedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    def search(self, item):
        current=self.head
        found=False
        while current!=None and found!=True:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found
    def remove(self,item):
        found=False
        current=self.head
        previous=None
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())

mylist = unorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print mylist.size()
print mylist.search(54)
print mylist.search(27)



