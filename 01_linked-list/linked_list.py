class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def to_list(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.value)
            node = node.next

        return nodes

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.next
        return found_nodes

    def delete(self, val, all=False):
        current = self.head
        previous = None

        while current is not None:
            if current.value != val:
                previous = current
                current = previous.next
                continue

            if previous is None:
                self.head = current.next
                previous = self.head
            else:
                previous.next = current.next

            if not all:
                break

            current = previous.next

        return self

    def clean(self):
        self.head = None
        self.tail = None

        return self

    def len(self):
        length = 0
        node = self.head

        while node is not None:
            length += 1
            node = node.next

        return length

    def insert(self, after_node, new_node):
        if after_node is not None:
            new_node.next = after_node.next
            after_node.next = new_node
            return self

        if self.head is None:
            self.add_in_tail(new_node)
        else:
            new_node.next = self.head.next
            self.head = new_node
