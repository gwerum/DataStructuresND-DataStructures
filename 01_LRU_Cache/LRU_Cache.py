import collections
import unittest
        
class LRU_Cache():
    def __init__(self, capacity = 5):
        # Initialize class variables
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            if not key: raise TypeError
            value = self.cache.pop(str(key))
            self.cache[str(key)] = value
            return value
        except (KeyError, TypeError):
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        try:
            if not key: raise TypeError
            self.cache.pop(str(key))
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        except TypeError:
            return -1
        self.cache[str(key)] = value


class TestCache(unittest.TestCase):
    """docstring for TestCache"""
    def setUp(self, cache_size = 5):
        self.cache_size = cache_size
        self.cache = LRU_Cache(self.cache_size)
        self.entries = {'1': 1, '10': 10, '37': 37, '14': 14, '5': 5}
        for key in self.entries:
            self.cache.set(key, self.entries[key])

    def test_cache_fill(self):
        self.assertEqual(self.cache.cache, self.entries)
        self.assertEqual(self.cache.get(1), 1)

    def test_cache_fill_strings(self):
        entries = {'A': 'a', 'D': 'd', 'M': 'm', 'X': 'x', 'Z': 'z'}
        for key in entries:
            self.cache.set(key, entries[key])
        self.assertEqual(self.cache.cache, entries)
        self.assertEqual(self.cache.get('Z'), 'z')
        self.assertEqual(self.cache.get('Y'), -1)

    def test_cache_fill_mixed_types(self):
        entries = {'1': [1, 3], '10': [10.26, 56.9678], \
                    'ABC': ['a', 'b', 'c'], '14': 14.572, '5': 5}
        for key in entries:
            self.cache.set(key, entries[key])
        self.assertEqual(self.cache.cache, entries)
        self.assertEqual(self.cache.get(10), [10.26, 56.9678])
        self.assertEqual(self.cache.get('ABC'), ['a', 'b', 'c'])

    def test_cache_overflow(self):
        overflow_entries = {'6': 6, '17': 17}
        for key in overflow_entries:
            self.cache.set(key, overflow_entries[key])
        self.assertEqual(self.cache.get(1), -1)
        self.assertEqual(self.cache.get(10), -1)

    def test_last_recently_used_order(self):
        self.assertEqual(self.cache.get(1), 1)
        overflow_entries = {'6': 6, '17': 17}
        for key in overflow_entries:
            self.cache.set(key, overflow_entries[key])
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(10), -1)

    def test_cache_fill_invalid_inputs(self):
        self.assertEqual(self.cache.set(None, None), -1)
        self.assertEqual(self.cache.cache, self.entries)

