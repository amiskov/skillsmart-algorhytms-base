"""
Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений,
и если их длины равны, возвращает список, каждый элемент которого равен
сумме соответствующих элементов входных списков.
"""

from linked_list import LinkedList


def sum_lists(l1, l2):
    if l1.len() != l2.len():
        return None

    l1_list = l1.to_list()
    l2_list = l2.to_list()
    result = []

    for idx, l in enumerate(l1_list):
        result.append(l + l2_list[idx])

    return LinkedList.from_list(result)


linked_list_1 = LinkedList.from_list([3, 13, 23, 33, 43, 53])
linked_list_2 = LinkedList.from_list([5, 15, 25, 35, 45, 55])
linked_list_3 = LinkedList.from_list([13, 33, 53])

empty_linked_list_1 = LinkedList.from_list([])
empty_linked_list_2 = LinkedList.from_list([])


def test_sum_lists():
    assert sum_lists(linked_list_1, linked_list_2).to_list() == [8, 28, 48, 68, 88, 108], \
        "Should be [8, 28, 48, 68, 88, 108]"
    assert sum_lists(empty_linked_list_1, empty_linked_list_2).to_list() == [], "Should be []"
    assert sum_lists(linked_list_1, linked_list_3) is None, "Should be None"


if __name__ == "__main__":
    test_sum_lists()
    print("Everything passed")
