class Node(object):
    def __init__(self, data, pnext=None):
        self.data = data
        self.next = pnext


class MyLinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def append(self, dataOrNode):
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1

    def delete(self, index):
        if self.is_empty():
            print("this chain table is empty.")

        if index < 0 or index >= self.length:
            print('error: out of index')

        if index == 0:
            self.head = self.head.next
            self.length -= 1

        j = 0
        node = self.head
        prev = node
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1

        if j == index:
            prev.next = node.next
            self.length -= 1

    def insert(self, index, dataOrNode):
        if self.is_empty():

            print("this chain tabale is empty")

        if index < 0 or index >= self.length:
            print("error: out of index")

        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1

        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def update(self, index, data):
        if self.is_empty() or index < 0 or index >= self.length:
            print('error: out of index')

            j = 0
            node = self.head
            while node.next and j < index:
                node = node.next
                j += 1

            if j == index:
                node.data = data

    def getItem(self, index):
        if self.is_empty() or index < 0 or index >= self.length:
            print("error: out of index")
        j = 0
        node = self.head
        while node.next and j < index:
            node = node.next
            j += 1

        return node.data

    def getIndex(self, data):
        j = 0
        if self.is_empty():
            print("this chain table is empty")
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node.next
            j += 1

        if j == self.length:
            print("%s not found" % str(data))

    def clear(self):
        self.head = None
        self.length = 0
