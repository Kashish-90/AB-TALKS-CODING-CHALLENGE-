# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Function to merge two sorted lists
def merge_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    # Attach remaining nodes
    if l1:
        tail.next = l1

    if l2:
        tail.next = l2

    return dummy.next


# First kingdom army
army1 = LinkedList()
army1.append(1)
army1.append(3)
army1.append(5)
army1.append(7)

# Second kingdom army
army2 = LinkedList()
army2.append(2)
army2.append(4)
army2.append(5)
army2.append(8)

print("Army 1:")
army1.display()

print("Army 2:")
army2.display()

# Merge armies
merged_head = merge_lists(army1.head, army2.head)

print("\nMerged Army:")

temp = merged_head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
