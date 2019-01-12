import unittest
from linked_list import Node
from linked_list import LinkedList


def create_linked_list_from_digits(digits):
    nodes = []
    linked_list = LinkedList()

    for digit in digits:
        nodes.append(Node(digit))

    for idx, node in enumerate(nodes):
        if idx != len(nodes) - 1:
            node.next = nodes[idx + 1]
        else:
            node.next = None
        linked_list.add_in_tail(node)

    return linked_list


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = create_linked_list_from_digits([3, 13, 23, 33, 43, 53])
        self.duplicated_list = create_linked_list_from_digits([55, 85, 55, 85, 95, 95])
        self.empty_list = create_linked_list_from_digits([])
        self.large_list = create_linked_list_from_digits(range(100))

    def test_add_in_tail(self):
        """
        Test if newly created linked list and linked list from self have
        equal list representation after adding new node.
        """
        new_linked_list = create_linked_list_from_digits([3, 13, 23, 33, 43, 53, 63])
        self.list.add_in_tail(Node(63))
        self.assertListEqual(new_linked_list.to_list(), self.list.to_list())
        self.assertEqual(2, 2)

    def test_to_list(self):
        self.assertListEqual([3, 13, 23, 33, 43, 53], self.list.to_list())

    def test_len(self):
        """
        Test if length of the prepared LinkedList is 6
        """
        self.assertEqual(6, self.list.len())

    def test_clean(self):
        self.assertEqual(0, self.list.clean().len())


if __name__ == '__main__':
    unittest.main()
