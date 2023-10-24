class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Largest:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
        self.top = node

    def Display(self):
        current = self.top

        while current:
            print(current.data, end='\n')
            current = current.next

    def largest(self):
        if self.top:
            current = self.top
            lar = current.data

            while current:
                if lar < current.data:
                    lar = current.data
                current = current.next
            return lar


a = Largest()
a.push(24)
a.push(33)
a.push(19)
a.push(8)
a.push(45)
a.push(39)
a.Display()
print()
a.largest()


