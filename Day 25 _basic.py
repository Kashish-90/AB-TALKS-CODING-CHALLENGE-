class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def create_cycle(self, position):
        if position == -1:
            return

        cycle_node = None
        temp = self.head
        count = 0

        while temp.next:
            if count == position:
                cycle_node = temp
            temp = temp.next
            count += 1

        temp.next = cycle_node

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# -------- Test Case 1 (No Cycle) --------
maze1 = LinkedList()

for i in range(1, 6):
    maze1.append(i)

print("Maze 1 has cycle:", maze1.detect_cycle())


# -------- Test Case 2 (Cycle Exists) --------
maze2 = LinkedList()

for i in range(1, 6):
    maze2.append(i)

maze2.create_cycle(2)

print("Maze 2 has cycle:", maze2.detect_cycle())


# -------- Test Case 3 (Another Cycle) --------
maze3 = LinkedList()

for i in range(10, 16):
    maze3.append(i)

maze3.create_cycle(0)

print("Maze 3 has cycle:", maze3.detect_cycle())
