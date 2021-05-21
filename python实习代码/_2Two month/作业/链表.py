class Node(object):
    def __init__(self,item):
        self.item=item
        self.next=None


class L(object):
    def __init__(self):
        self.head=None

    def add(self,item):
        node=Node(item)
        if self.head is None:
            node.next=self.head
            self.head=node

        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=node

    def length(self):
        count=0
        if self.head is None:
            return 0
        else:
            cur=self.head
            while cur is not None:
                count+=1
                cur=cur.next
        return count

    def insert(self,pos,item):
        node=Node(item)
        if pos<=0:
            node.next=self.head
            self.head=node
        elif pos>=self.length():
            self.add(item)
        else:
            count=0
            pre=None
            cur=self.head
            while cur is not None:
                pre=cur
                cur=cur.next
                count += 1
                if pos==count:
                    pre.next=node
                    node.next=cur
                    break

    def gai(self,pos,item):
        node=Node(item)
        cur=self.head
        pre=None
        if pos<=0:
            node.next=cur.next
            self.head=node
        elif pos>=self.length():
            while cur.next is not None:
                pre=cur
                cur=cur.next
            pre.next=node
        else:
            count=0
            while cur.next is not None:
                count+=1
                pre=cur
                cur=cur.next
                if pos==count:
                    pre.next=node
                    node.next=cur.next
                    break


    def travle(self):
        if self.head is None:
            return
        else:
            cur=self.head
            while cur is not None:
                print(cur.item)
                cur=cur.next



l=L()
l.add(1)
l.add(2)
l.insert(0,3)
l.insert(1,4)
l.insert(9,9)
l.gai(0,8)
l.gai(1,6)
l.gai(10,3)
l.travle()
# print(l.length())


















