
# Stack implementation using list (array)
stack = [43,22,78,64]   # empty stack
MAX_SIZE = 5 

def push():
    if len(stack) == MAX_SIZE:
        print("Stack Overflow!")
    else:
        element = input("Enter element to push: ")
        stack.append(element)
        print(f"{element} pushed onto stack.")

def pop():
    if not stack:
        print("Stack Underflow! Stack is empty.")
    else:
        element = stack.pop()
        print(f"Popped element: {element}")

def peek():
    if not stack:
        print("Stack is empty. Nothing to peek.")
    else:
        print(f"Top element: {stack[-1]}")

def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack elements (top to bottom):")
        for i in reversed(stack):
            print(i)

# Menu-driven program
while True:
    print("\n==== STACK MENU ====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
