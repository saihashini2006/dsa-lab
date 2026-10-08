queue = []
MAX_SIZE = 5

def enqueue():
    if len(queue) == MAX_SIZE:
        print("Queue Overflow")
    else:
        x = int(input("Enter element: "))
        queue.append(x)
        print(x, "enqueued")

def dequeue():
    if not queue:
        print("Queue Underflow")
    else:
        print("Dequeued:", queue.pop(0))

def peek():
    if not queue:
        print("Queue is empty")
    else:
        print("Front element:", queue[0])

def display():
    if not queue:
        print("Queue is empty")
    else:
        print("Queue elements:", queue)

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