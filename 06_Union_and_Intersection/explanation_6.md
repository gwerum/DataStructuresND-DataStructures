## Explanation for union_intersection.py

### Code explanation & Data Structures

The goal of this exercise is to implement the following methods:

* **get_llist_intersection(*llist_1, llist_2*)**: returns a linked list with all nodes belonging to the intersection (without repetition) of the linked lists *llist_1* and *llist_2*. The original order remains and nodes of *llist_1* will come before nodes of *list_2*.

* **get_llist_union(*llist_1, llist_2*)**: returns a linked list with all nodes belonging to the union (without repetition) of the linked lists *llist_1* and *llist_2*. The original order remains and nodes of *llist_1* will come before nodes of *list_2*. Since the union of two sets also contains the intersection of those sets the *get_llist_union()* method makes use of the *get_llist_intersection()* method and calls it within its function scope. 

There are not additional helper methods defined. However, within the scope of the **class LinkedList()** the two operator methods **\_\_iter\_\_()** and **\_\_contains\_\_()** have been defined to ease the ability of "walking" through the values stored in the linked list.

---

### Runtime efficiency

**Get values_1 from llist_1**: For computing the intersection in the first step one has to retrieve all values of *llist_1* and check if they exist in *llist_2*. Time complexity of walking through all values is of order O(n), space complexity is constant due to the implementation of *\_\_iter\_\_()* as generator method.

**Check if value_1 exists in llist_2**: Checking if a value exists in a single linked list always means to walking the list from head to tail. This means in best case O(1) and in worst case O(n). However, the average time complexity can be estimated to be O(n/2) assuming the union values of *llist1* and *llist2* to be equally distributed over linked list *llist_2*. This process has to be done for each value of *llist_1*.

**Create resulting linked list**: Creating one node comes with constant time and space complexity. Thus, total time and space complexity will be both O(m), considering m the total number of union values.

**Check for repetition**: Checking for repetition comes at the cost of checking the temporary result list for values, but reduces the number of searches performed on *llist_2*. Since m is usually smaller then n it is worth the effort. Additionaly, m is only the final length of the result list, thus, average time complexity of the repetition search can be assumed to be O(m/2).

| **get_llist_intersection(*llist_1, llist_2*)** | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| Check if values_1 exist in llist_2 | O(n\*(n/2)) | |
| Create resulting linked list | O(m) | O(m) |
| Check for repetition | O(m/2) |  |
| **Total** | **O(n\*(n/2) + 3m/2) ~ O(n^2)** | **O(m)** |

**n**: number of nodes in llist_1 and llist2 respectively, assuming equal length
**m**: number of intersection nodes

Computing the union doesn't required checking the existance of values_1 in *llist_2*. Values from both lists *llist_1* and *llist_2* will be read and added to the resulting list. Checking for repetition comes in this case with a higher cost since the resulting list is almost of length 2n. 

| **get_llist_union(*llist_1, llist_2*)** | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| Read & add values_1 to union list | O(n) | O(n) |
| Check for repetition | O(n/2) |  |
| Read & add values_1 to union list | O(n) | O(n-m) |
| Check for repetition | O(n + (n-m)/2) |  |
| **Total** | **O(4n - m/2) ~ O(4n)** | **O(2n - m) ~ O(2n)** |

**n**: number of nodes in llist_1 and llist2 respectively, assuming equal length
**m**: number of intersection nodes

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