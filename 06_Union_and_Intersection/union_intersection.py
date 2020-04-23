import unittest
from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def __str__(self):
        output_string = ""
        for value in self.__iter__():
            output_string += str(value) + " -> "
        return output_string[:-4]

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __contains__(self, value):
        if self.is_empty():
            return False
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def is_empty(self):
        return self.num_elements == 0

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            self.num_elements += 1
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.num_elements += 1

def get_llist_union(llist_1, llist_2):
    # Your Solution Here
    llist_union = LinkedList()
    for value_1 in llist_1:
        if value_1 not in llist_union:
            llist_union.append(value_1)
    for value_2 in llist_2:
        if value_2 not in llist_union:
            llist_union.append(value_2)
    return llist_union

def get_llist_intersection(llist_1, llist_2):
    # Your Solution Here
    llist_intersection = LinkedList()
    for value_1 in llist_1:
        if value_1 not in llist_intersection:
            if value_1 in llist_2:
                llist_intersection.append(value_1)
    return llist_intersection


class TestintersectionAndUnion(unittest.TestCase):
    """docstring for Testintersection"""
    def test_union_with_integers(self):
        print("Test1: test union with integers")
        set_1 = [3,2,4,35,6,65,6,4,3,21]
        set_2 = [6,32,4,9,6,1,11,21,1]
        llist_1, llist_2 = self.__create_linked_lists(set_1, set_2)

        expected_union = self.__get_list_union(set_1, set_2)
        llist_union = get_llist_union(llist_1, llist_2)

        self.__check_union(llist_union, expected_union)
        pass

    def test_intersection_with_integers(self):
        print("Test2: test intersection with integers")
        set_1 = [3,2,4,35,6,65,6,4,3,21]
        set_2 = [6,32,4,9,6,1,11,21,1]
        llist_1, llist_2 = self.__create_linked_lists(set_1, set_2)

        expected_intersection = self.__get_list_intersection(set_1, set_2)
        llist_intersection = get_llist_intersection(llist_1, llist_2)

        self.__check_intersection(llist_intersection, expected_intersection)
        pass

    def test_union_with_strings(self):
        print("Test3: test union with strings")
        set_1 = ["Apple","Mango","Peach","Banana","Watermelon"]
        set_2 = ["Banana","Orange","Grapes","Watermelon","Tomato"]
        llist_1, llist_2 = self.__create_linked_lists(set_1, set_2)

        expected_union = self.__get_list_union(set_1, set_2)
        llist_union = get_llist_union(llist_1, llist_2)

        self.__check_union(llist_union, expected_union)
        pass

    def test_intersection_with_strings(self):
        print("Test4: test intersection with strings")
        set_1 = ["Apple","Mango","Peach","Banana","Watermelon"]
        set_2 = ["Banana","Orange","Grapes","Watermelon","Tomato"]
        llist_1, llist_2 = self.__create_linked_lists(set_1, set_2)

        expected_intersection = self.__get_list_intersection(set_1, set_2)
        llist_intersection = get_llist_intersection(llist_1, llist_2)

        self.__check_intersection(llist_intersection, expected_intersection)
        pass

    def test_union_with_large_array(self):
        print("Test5: test union with large integer array")
        set_1 = [randint(0,100) for _ in range(1000)]
        set_2 = [randint(0,100) for _ in range(1000)]
        llist_1, llist_2 = self.__create_linked_lists(set_1, set_2)

        expected_union = self.__get_list_union(set_1, set_2)
        llist_union = get_llist_union(llist_1, llist_2)

        self.__check_union(llist_union, expected_union)
        pass

    def test_intersection_with_large_array(self):
        print("Test6: test intersection with large integer array")
        set_1 = [randint(0,100) for _ in range(1000)]
        set_2 = [randint(0,100) for _ in range(1000)]
        llist_1, llist_2 = self.__create_linked_lists(set_1, set_2)

        expected_intersection = self.__get_list_intersection(set_1, set_2)
        llist_intersection = get_llist_intersection(llist_1, llist_2)

        self.__check_intersection(llist_intersection, expected_intersection)
        pass

    def test_union_with_no_intersection(self):
        print("Test7: test union with no intersection of example set")
        set_1 = [3,2,4,35,6,65,6,4,3,23]
        set_2 = [1,7,8,9,11,21,1]
        llist_1, llist_2 = self.__create_linked_lists(set_1, set_2)

        expected_union = self.__get_list_union(set_1, set_2)
        llist_union = get_llist_union(llist_1, llist_2)

        self.__check_union(llist_union, expected_union)
        pass

    def test_intersection_with_no_intersection(self):
        print("Test8: test intersection with no intersection of example set")
        set_1 = [3,2,4,35,6,65,6,4,3,23]
        set_2 = [1,7,8,9,11,21,1]
        llist_1, llist_2 = self.__create_linked_lists(set_1, set_2)

        expected_intersection = self.__get_list_intersection(set_1, set_2)
        llist_intersection = get_llist_intersection(llist_1, llist_2)

        self.__check_intersection(llist_intersection, expected_intersection)
        pass

    def __create_linked_lists(self, set_1, set_2):
        llist_1 = self.__create_linked_list_from(set_1)
        llist_2 = self.__create_linked_list_from(set_2)
        return llist_1, llist_2

    def __create_linked_list_from(self, values_list):
        linked_list = LinkedList()
        for value in values_list:
            linked_list.append(value)
        return linked_list

    def __get_list_union(self, set_1, set_2):
        return sorted(list(set(set_1) | set(set_2)))

    def __get_list_intersection(self, set_1, set_2):
        return sorted(list(set(set_1) & set(set_2)))

    def __check_union(self, llist_union, expected_union):
        llist_values = []
        for value in llist_union:
            llist_values.append(value)
        if len(expected_union) < 20:
            print("Resulting llist: {}".format(llist_union))
            print("Expected values: {}".format(expected_union))
            print("Result values: {}".format(sorted(llist_values))+'\n')
        else:
            print("Results not printed, because too large \n")
        self.assertEqual(sorted(llist_values),expected_union)

    def __check_intersection(self, llist_intersection, expected_intersection):
        llist_values = []
        for value in llist_intersection:
            llist_values.append(value)
        if len(expected_intersection) < 20:
            print("Resulting llist: {}".format(llist_intersection))
            print("Expected values: {}".format(expected_intersection))
            print("Result values: {}".format(sorted(llist_values))+'\n')
        else:
            print("Results not printed, because too large \n")
        self.assertEqual(sorted(llist_values), expected_intersection)
        

