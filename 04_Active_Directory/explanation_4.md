## Explanation for union_intersection.py

### Code explanation & Data Structures

The goal of this exercise is to implement the method **is_member_in_group(*member, group*)**, which searches an *Active Directory*-type tree structure and checks for membership. Each node of the tree represents a group, each group has a name, a list of sub-groups and members:
```
class Group():
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.members = []
```

 The **is_member_in_group(*member, group*)** method returns **TRUE** if a member is member of the particular group or member of at least one of the sub-groups of that group. The implementation of this method is pretty straight-forward and is implemented in a recursive manner. It returns TRUE as soon as one positive membership is found and doesn't check the remaining groups.

 The challenge of this exercise is not so much the implementation of the method but rather the testing methods. For testing purposes an input dictionary with groups is provided and used to construct the directory tree. In the following the dictionary is also used for the validation of the **is_member_in_group(*member, group*)** method.

---

### Runtime efficiency

As described above, the **is_member_in_group(*member, group*)** method stops as soon as the first positive membership is found. This prevents the method from going too deep into the tree if not necessary. The runtime efficiency of course depends highly on where the member is located in the tree, which leads to best case O(1) and worst case O(n). A better estimation of the runtime efficiency would be possible if the directory tree would have been implemented as a binary search tree (which hasn't been done in this exercise). In the latter case, the worst case runtime could be estimated to be of order O(log(n))

|  | Time complexity | Space complexity | Decription |
| ------------------- | --------------- | ---------------- | ---------------- |
| Worst case | O(n) | O(d) | If all nodes of the tree need to be searched |
| Best case | O(1) | O(1) | If the member is member of the first group searched |
| Worst case BST | O(log(n)) | O(log(n)) | If the directory would have been implemented as BST |

**n**: total number of nodes in directory tree
**d**: tree depths

---

### Test Cases

The following test cases have been created to test base and corner use cases:

1. Test 'Family' directory tree of depths 3 and widths 1
2. Test 'Numbers' directorry tree of depths 4 and widths 2 plus multiple references to same group/node

Running the tests can be executed using the following command:

```
python -m unittest ActiveDirectory.py
```