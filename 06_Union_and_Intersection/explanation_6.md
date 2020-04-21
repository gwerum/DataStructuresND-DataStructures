## Explanation for union_intersection.py

### Code explanation & Data Structures

The goal of this exercise was to implement the methods **get_llist_union(llist_1, llist_2)** and **get_llist_intersection(llist_1, llist_2)**, which respectively compute the union and intersection of two linked lists provided as arguments. Both methods return linked lists of union and intersection respectively maintaining the original list orders without repetition. In case of the union the values of llist_1 will appear before the values of llist_2.

Since the union of two sets also contains the intersection of those sets the *get_llist_union()* method makes use of the *get_llist_intersection()* method and calls it within its function scope. There are not additional helper methods defined. However, within the scope of the LinkedList class definition the two operator methods **__iter__()** and **__contains__()** have been defined to ease the ability of "walking" through the values stored in the linked list.

---

### Runtime efficiency

For computing the intersection one has to walk through all values of **llist_1** and check if they exist in **llist_2**. Time complexity of walking through all values is of order O(n), space complexity is constant due to the implementation of **__iter__()** as generator method.
Checking if the values from llist_1 are contained in llist_2 has a time complexity of in best case O(1) and in worst case O(n), however the average time complexity can be estimated to be O(n/2) assuming the union values of llist1 and llist2 to be equally distributed over linked list llist_2. This process however is done for each (unique) value of llist_1, thus, time complexity will be worst case O(n\*(n/2)) if only unique values are contained in llist_1 and llist_2. Checking for repetition reduces on the one side the number of value searches in llist_2, but comes with the worst case time cost of order O(m/2) in each cycle n. So, overall time cost for searching a value in llist_2 can be approximated with O(n\*(n/2 + m/2)) ~ O(n^2).
Creating the resulting linked list with needs to append each matching value to the resulting linked list. The **append(value)** method of the linked list is implemented with constant time complexity, thus, time and space complexity will be respectively O(m), consider m the total number of union values.

| **get_llist_intersection(llist_1, llist_2)** | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| Walk values of llist_1 | O(n) | O(1) |
| Check if value in llist_2 | O(n^2) | |
| Create resulting linked list | O(m) | O(m) |
| **Total** | **O(n^2 + n + m) ~ O(n^2)** | **O(m + 1) ~ O(m)** |

**n**: number of nodes in llist_1 and llist2 respectively, assuming equal length
**m**: number of union nodes

Computing the union requires additional to computing the intersection walking of list llist_1 and llist_2, which is both of time cost O(n). Again, the number of matching nodes need to be added to the resulting linked list, which is of time and space complexity O(2\*(n-m)).

| **get_llist_union(llist_1, llist_2)** | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| Get intersection | O(n^2) | O(m) |
| Walk list llist_1 | O(n) | |
| Walk list llist_2 | O(n) | |
| Create resulting linked list | O(2\*(n-m)) | O(2\*(n-m)) |
| **Total** | **O(n^2 + 4\*n - 2\*m) ~ O(n^2)** | **O(2\*n - m) ~O(n)** |

**n**: number of nodes in llist_1 and llist2 respectively, assuming equal length
**m**: number of union nodes

---

### Test Cases

The following test cases have been created to test base and corner use cases:

1. Test union method with integer values
2. Test intersection method with integer values
3. Test union method with string values
4. Test intersection method with string values
5. Test union method with large integer array
6. Test intersection method with large integer array
7. Test union method with no intersection
8. Test intersection method with no intersection

Running the tests can be executed using the following command:

```
python -m unittest union_intersection.py
```