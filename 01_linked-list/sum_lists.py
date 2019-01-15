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

    return result


l1 = LinkedList.from_list([3, 13, 23, 33, 43, 53])
l2 = LinkedList.from_list([3, 13, 23, 33, 43, 53])
l3 = LinkedList.from_list([13, 33, 53])

l_empty1 = LinkedList.from_list([])
l_empty2 = LinkedList.from_list([])


def test_sum_lists():
    assert sum_lists(l1, l2) == [6, 26, 46, 66, 86, 106], "Should be [6, 26, 46, 66, 86, 106]"
    assert sum_lists(l_empty1, l_empty2) == [], "Should be []"
    assert sum_lists(l1, l3) is None, "Should be None"


if __name__ == "__main__":
    test_sum_lists()
    print("Everything passed")
