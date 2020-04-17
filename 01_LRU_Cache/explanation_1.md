# LRU_Cache.py

## Code explanation & Data structures

The tasks of this exercise was to implement a class for a `Last-Recently-Used-Cache (LRU Cache)` of size 5 for storing *key-value-pairs*, including a `get(key)` and `set(key, value)` method. From this task the requirements can be derived:

1. **Storage of key-value-pairs**: using a dict is the standard data structure in Python for storing *key-value-pairs*. However, the standard dict comes with a short-coming since it is unordered and therefore makes it difficult to satisfy the *Last-Recently-Used* requirement.

2. **Maximum 5 elements in cache**: The cache size is limited to maximum 5 elements, therefore only the five least recently used elements shall be kept in the cache.

3. **Last-Recently-Used order**: the LRU requirement requires a queue-like data structure, so that the oldest key-value-pair will be removed in case of cache overflow.

4. **Access to all cache elements**: All key-value-pairs stored in the cache shall be accessible at all times, not only head and/or tail elements. Therefore, a doubly-linked-list type data structure is required.

There is an existing data structure, which satisfies already requirement 1, 4 and partly requirement 3, it is the `OrderedDict()` from the `collections` library. The `OrderedDict()` is similar to the standard Python dict with the additional feature, that it *remembers* the order of the elements, that have been added to it. I therefore chose this data structure as my base data structure for implementing the cache.

To fulfill all requirements stated above I had to limit the size of the ordered dict to maximum five elements. If the cache size is already five, then the `set(key, value)` method will take care, that the oldest element is removed from the cache. If any cache element is acessed, the `get(key)` method will take care to *enqueue* the element to the *cache tail* after acessing it.

---

## Runtime efficiency

Let's consider N the average size of an element stored in the cache, then the space requirements are O(5N). The cache is implemented as dictionary, which are implemented as hashmaps in Python. The worst case access time is *O(n)*, however in average a constant access time, for both read and write, can be assumed, especially in case the dict is small as the cache.

The *get(key)* method requires one read and one write access, therefor O(2). The same applies for the *set(key, value)* method, since it needs to be checked if the element already exists in the cache. In case of cache overflow the oldest element needs to be removed, so the worst case for the *set(key, value)* method is O(3). The worst case time complexity of any cache access method is therefore O(3) = max(O(2),O(3)).

|  | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| single call of *get(key)* | O(2) | |
| single call of *set(key, value)* | O(3) | O(N) |
| **Total cache** | **O(3)** | **O(5N)** |

**N**: Average size of element stored in cache

---

## Test Cases

Six test cases have been implemented in `class TestCache()` for the following default and corner use cases:

1. **Cache fill: integers**: cache filled with 5 key-integer-pairs
2. **Cache fill: string**: cache filled with 5 key-string-pairs
3. **Cache fill: mixed types**: cache filled with 5 key-value-pairs including integers, strings, floats, string arrays, float arrays, integer arrays.
4. **Cache overflow**: checks that old elements are removed first in case of cache overflow
5. **Cache LRU order**: checks that least recently used elements are correctly moved to cache queue tail
6. **Invalid inputs**: checks that null entries are not added to cache.

The test cases can be executed using the following command:

```
python -m unittest LRU_Cache.py
```