import random  # to import random integers
import time    # to import time sleep


class Node:   # node to add messages in the queue
    def __init__(self, data):
        self.data = data
        self.next = None


class ATTEMPTS:   # node to count the number of messages in each attempts
    def __init__(self, data):
        self.data = data
        self.next = None


class Queues:

    # declaring global variables
    processed = 0
    total_arvl = 0
    count = 0
    requeue = 0

    def __init__(self):
        self.front = None  # this is for messages to add in the queue
        self.rear = None   # this is for messages to add in the queue

        self.head = None   # this is for the attempts

    def Enqueue(self, data):
        node = Node(data)

        if self.front:
            current = self.front

            while current.next:
                current = current.next
            current.next = node
            self.rear = node

        else:
            self.front = self.rear = node

    def dequeue(self):

        if self.front:
            self.front = self.front.next

        else:
            print("Queue is empty")

    def add_attempts(self, data):   # methods to add the number of messages sent in every attempts
        attempts = ATTEMPTS(data)

        if self.head:
            current = self.head

            while current.next:
                current = current.next
            current.next = attempts

        else:
            self.head = attempts

    def Email(self):  # methods for email simulation
        process_rate = 40
        arrival_rate = 30
        Time = 1440  # Total time in minutes (24 hours)

        for t in range(Time):
            arrival = random.randint(0, arrival_rate)
            Q.total_arvl += arrival  # counting all the arrival messages each minute

            for i in range(1, arrival + 1):
                self.Enqueue("MESSAGE %d Cannot be sent" % i)
                Q.count += 1  # counting all the enqueue messages

            processing = random.randint(0, process_rate)
            current = self.front
            for i in range(1, processing + 1):
                while current:
                    if current.data and random.uniform(0, 1) > 0.25:  # 25% of the messages in the queue cannot be sent
                        self.dequeue()
                        Q.processed += 1
                    else:
                        Q.requeue += 1
                    current = current.next

            time.sleep(60)   # timer
        self.add_attempts(Q.processed)

    def Total_Messages(self):
        print('\nTotal message processed %d' % Q.processed)

    def average_arrival(self):
        avg_arvl = Q.total_arvl / 2

        print("The average arrival rate: %.1f" % avg_arvl)

    def avg_sent_per_minute(self):
        average_sent = Q.processed / 2

        print("The average number of messages sent per minute: %.1f" % average_sent)

    def avg_msg_queue(self):
        avg_msg = Q.count / 2

        print("The average number of messages in the queue in a minute: %.1f" % avg_msg)

    def messages_requeued(self):
        print("The average number of times messages had to be requeued:", Q.requeue)

    def display_attempts(self):
        current = self.head
        count = 0

        while current:
            count += 1
            print("Attempt %d: %d messages sent" % (count, current.data), end='\n')
            current = current.next


Q = Queues()

count = 0


print("1. Start the simulation")
print("2. View the total message process")
print("3. View the average arrival rate")
print("4. View the average number of messages sent per minute")
print("5. View the average number of messages in the queue in a minute")
print("6. View the number of messages sent on the first attempt, the second attempt, and so forth")
print("7. View the average number of times messages had to be requeued")
print("0. Exit")

choice = int(input("\nEnter your choice: "))

while choice == 1:
    Q.Email()
    count += 1

    press = input("\nSimulation done! press 'x' if you want to exit: ")
    print()
    if press.lower() == 'x':
        break

while choice == 2:
    Q.Total_Messages()

    press = input("\nPress any key to add again and press 'x' if you want to exit: ")
    print()
    if press.lower() == 'x':
        break

while choice == 3:
    Q.average_arrival()

    press = input("\nPress any key to add again and press 'x' if you want to exit: ")
    print()
    if press.lower() == 'x':
        break

while choice == 4:
    Q.avg_sent_per_minute()

    press = input("\nPress any key to add again and press 'x' if you want to exit: ")
    print()
    if press.lower() == 'x':
        break

while choice == 5:
    Q.avg_msg_queue()

    press = input("\nPress any key to add again and press 'x' if you want to exit: ")
    print()
    if press.lower() == 'x':
        break

while choice == 6:
    Q.display_attempts()

    press = input("\nPress any key to add again and press 'x' if you want to exit: ")
    print()
    if press.lower() == 'x':
        break

while choice == 7:
    Q.messages_requeued()

    press = input("\nPress any key to add again and press 'x' if you want to exit: ")
    print()
    if press.lower() == 'x':
        break
