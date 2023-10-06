class Node:
    datas = 0
    next = None
    def __init__(self,data):
        self.data = data
        self.next = None

    def printdata(self):
        print(self.data)

    def changeclassvariable(self):
        self.datas = 100


class LinkedList:
    def __init__(self,head):
        self.head = None

node = Node(3)
secondnode = Node(4)
node.printdata()

print(node.datas)
print(secondnode.datas)
print(node.next)

node.changeclassvariable()
print(node.datas)
print(secondnode.datas)