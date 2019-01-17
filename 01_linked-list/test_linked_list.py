import unittest
from linked_list import Node
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """
        Creates some linked lists for tests.
        """
        self.empty_linked_list = LinkedList.from_list([])
        self.one_node_linked_list = LinkedList.from_list([1])
        self.small_linked_list = LinkedList.from_list([3, 13, 23, 33, 43, 53])
        self.large_linked_list = LinkedList.from_list(range(100))
        self.duplicated_linked_list = LinkedList.from_list([55, 85, 55, 85, 95, 95])

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

        duplicated_in_tail = LinkedList.from_list([22, 22, 22])
        duplicated_in_tail.delete(22)
        self.assertListEqual([22, 22], duplicated_in_tail.to_list())

        delete_from_tail_list = LinkedList.from_list([11, 21, 31])
        delete_from_tail_list.delete(31)
        print(delete_from_tail_list.tail.value)
        self.assertListEqual([11, 21], delete_from_tail_list.to_list())
        self.assertEqual(delete_from_tail_list.head.value, 11)
        self.assertEqual(delete_from_tail_list.tail.value, 21)

    def test_delete_all(self):
        self.empty_linked_list.delete(1, True)
        self.assertIs(None, self.empty_linked_list.head)
        self.assertIs(None, self.empty_linked_list.tail)

        self.one_node_linked_list.delete(1, True)
        self.assertListEqual([], self.one_node_linked_list.to_list())
        self.assertIs(None, self.one_node_linked_list.head)
        self.assertIs(None, self.one_node_linked_list.tail)

        self.duplicated_linked_list.delete(55, True)
        self.assertEqual([85, 85, 95, 95], self.duplicated_linked_list.to_list())
        self.assertIs(85, self.duplicated_linked_list.head.value)
        self.assertIs(95, self.duplicated_linked_list.tail.value)

        duplicated_in_tail = LinkedList.from_list([23, 22, 22])
        duplicated_in_tail.delete(22, True)
        self.assertListEqual([23], duplicated_in_tail.to_list())
        self.assertIs(23, duplicated_in_tail.head.value)
        self.assertIs(23, duplicated_in_tail.tail.value)

        equal_nodes_list = LinkedList.from_list([22, 22, 22])
        equal_nodes_list.delete(22, True)
        self.assertListEqual([], equal_nodes_list.to_list())
        self.assertIs(None, equal_nodes_list.head)
        self.assertIs(None, equal_nodes_list.tail)

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

        linked_list.insert(nodes[0], Node(64))
        self.assertListEqual([2, 64, 4, 8, 32, 16], linked_list.to_list())

        linked_list.insert(nodes[3], Node(128))
        self.assertListEqual([2, 64, 4, 8, 32, 16, 128], linked_list.to_list())
        self.assertEqual(128, linked_list.tail.value)

        empty_linked_list = LinkedList()
        empty_linked_list.insert(empty_linked_list.head, Node(256))
        self.assertListEqual([256], empty_linked_list.to_list())
        self.assertEqual(empty_linked_list.head.value, 256)
        self.assertEqual(empty_linked_list.tail.value, 256)


if __name__ == '__main__':
    unittest.main()
