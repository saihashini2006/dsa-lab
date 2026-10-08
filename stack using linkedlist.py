class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

front = rear = None

def enqueue():
    global front, rear
    x = int(input("Enter element: "))
    new = Node(x)

    if rear is None:
        front = rear = new
    else:
        rear.next = new
        rear = new

    print(x, "enqueued")

def dequeue():
    global front, rear
    if front is None:
        print("Queue Underflow")
    else:
        print("Dequeued:", front.data)
        front = front.next

        if front is None:
            rear = None

def peek():
    if front is None:
        print("Queue is empty")
    else:
        print("Front element:", front.data)

def display():
    if front is None:
        print("Queue is empty")
    else:
        temp = front
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")