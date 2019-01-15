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
        """
        Creates some linked lists for tests.
        """
        self.empty_linked_list = create_linked_list_from_digits([])
        self.one_node_linked_list = create_linked_list_from_digits([1])
        self.small_linked_list = create_linked_list_from_digits([3, 13, 23, 33, 43, 53])
        self.large_linked_list = create_linked_list_from_digits(range(100))
        self.duplicated_linked_list = create_linked_list_from_digits([55, 85, 55, 85, 95, 95])

    def test_add_in_tail(self):
        self.empty_linked_list.add_in_tail(Node(63))
        self.small_linked_list.add_in_tail(Node(63))
        self.large_linked_list.add_in_tail(Node(63))

        self.assertListEqual([3, 13, 23, 33, 43, 53, 63], self.small_linked_list.to_list())
        self.assertListEqual([63], self.empty_linked_list.to_list())
        self.assertListEqual([*range(100), 63], self.large_linked_list.to_list())

    def test_to_list(self):
        self.assertListEqual([], self.empty_linked_list.to_list())
        self.assertListEqual([1], self.one_node_linked_list.to_list())
        self.assertListEqual([3, 13, 23, 33, 43, 53], self.small_linked_list.to_list())
        self.assertListEqual([*range(100)], self.large_linked_list.to_list())

    def test_print_all_nodes(self):
        pass

    def test_find(self):
        n1 = Node(255)
        n2 = Node(255)
        n1.next = n2

        self.small_linked_list.add_in_tail(n1)
        self.duplicated_linked_list.add_in_tail(n1)
        self.large_linked_list.add_in_tail(n1)

        self.assertIs(None, self.empty_linked_list.find(1))
        self.assertEqual(1, self.one_node_linked_list.find(1).value)

        self.assertEqual(n1, self.small_linked_list.find(255))
        self.assertEqual(n1, self.duplicated_linked_list.find(255))
        self.assertEqual(n1, self.large_linked_list.find(255))

    def test_find_all(self):
        n1 = Node(255)
        n2 = Node(255)
        n1.next = n2

        self.small_linked_list.add_in_tail(n1)
        self.duplicated_linked_list.add_in_tail(n1)
        self.large_linked_list.add_in_tail(n1)

        self.assertListEqual([], self.empty_linked_list.find_all(1))
        self.assertEqual(1, len(self.one_node_linked_list.find_all(1)))

        self.assertListEqual([n1, n2], self.small_linked_list.find_all(255))
        self.assertListEqual([n1, n2], self.duplicated_linked_list.find_all(255))
        self.assertListEqual([n1, n2], self.large_linked_list.find_all(255))

    def test_delete(self):
        self.empty_linked_list.delete(1)
        self.assertIs(None, self.empty_linked_list.head)
        self.assertIs(None, self.empty_linked_list.tail)

        self.one_node_linked_list.delete(1)
        self.assertListEqual([], self.one_node_linked_list.to_list())

        self.duplicated_linked_list.delete(55)
        self.assertEqual([85, 55, 85, 95, 95], self.duplicated_linked_list.to_list())

    def test_delete_all(self):
        self.empty_linked_list.delete(1, True)
        self.assertIs(None, self.empty_linked_list.head)
        self.assertIs(None, self.empty_linked_list.tail)

        self.one_node_linked_list.delete(1, True)
        self.assertListEqual([], self.one_node_linked_list.to_list())

        self.duplicated_linked_list.delete(55, True)
        self.assertEqual([85, 85, 95, 95], self.duplicated_linked_list.to_list())

    def test_clean(self):
        self.assertEqual(0, self.empty_linked_list.clean().len())
        self.assertEqual(0, self.one_node_linked_list.clean().len())
        self.assertEqual(0, self.small_linked_list.clean().len())
        self.assertEqual(0, self.large_linked_list.clean().len())

    def test_len(self):
        self.assertEqual(0, self.empty_linked_list.len())
        self.assertEqual(1, self.one_node_linked_list.len())
        self.assertEqual(6, self.small_linked_list.len())
        self.assertEqual(100, self.large_linked_list.len())

    def test_insert(self):
        self.one_node_linked_list.insert(self.one_node_linked_list.head, Node(128))
        self.assertEqual([1, 128], self.one_node_linked_list.to_list())

        linked_list = LinkedList()
        nodes = [Node(2), Node(4), Node(8), Node(16)]
        for idx, node in enumerate(nodes):
            if idx != len(nodes) - 1:
                node.next = nodes[idx + 1]
            else:
                node.next = None
            linked_list.add_in_tail(node)
        linked_list.insert(nodes[2], Node(32))
        self.assertListEqual([2, 4, 8, 32, 16], linked_list.to_list())


if __name__ == '__main__':
    unittest.main()
