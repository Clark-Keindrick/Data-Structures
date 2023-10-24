class Node:  # creating a node template
    def __init__(self, data):
        self.data = data
        self.next = None


class Stacks:  # creating a class for stacks
    def __init__(self):
        self.top = None

    def push(self, data):  # Method for adding a node in the stacks
        node = Node(data)

        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):  # Method to delete a node in the stacks
        if self.top:
            self.top = self.top.next

        else:
            print("List is Empty")

    def display(self):  # Method to display all the nodes in the stacks
        current = self.top
        count = 6

        while current:
            count -= 1
            print(current.data, end=' ')
            current = current.next
            if count == 1:
                break
        print()


s = Stacks()  # object instantiation
count = 1  # count variable to set a limitation
j = 1  # j variable to count the user's input

while True:

    num = int(input())
    s.push(num)
    j += 1

    if num > 0:  # condition that only positive integers will be counted
        count += 1

    if count <= 22:  # condition that limit the user's input up to 22 positive integers only
        if num < 0:  # condition that will delete a negative integer and will display the stacks
            s.pop()
            print()
            s.display()

            if j <= 5:  # condition that stop the program if ever the items in the stacks are fewer than five
                print("\nYou entered fewer than five items in the stack")
                break
    else:  # if the user's input reached the limit
        # it will display the remaining items in the stacks and stop the program
        print("\nThank you for filling the Stacks !!!")
        s.display()
        break
