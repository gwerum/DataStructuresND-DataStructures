## Blockchain.py

### Code explanation & Data Structures

The base data structure of a blockchain is a (single) linked list, which can only be traversed from its end (tail) to its source (head). New blocks are always added to its end, the first block of the chain is called genesis block. The difference to a standard linked list is, that it uses hash pointers instead of memory pointers to link to the previous element in the list (previous block in the blockchain). 

Hash pointers are comprised of two parts:

* Pointer to where some information is stored (pointer to memory location of previous block)
* Cryptographic hash of that information (hash of the information stored in the previous block)

So, a hash pointer can not only be used to get the information from the previous block, but also is used to verify that this information hasn't been changed since creation of the block.

![alt text](https://github.com/gwerum/DataStructuresND-DataStructures/05_Blockchain/hash_pointer "Use of hash pointers in block chain ")

---

### Runtime efficiency


```
Time complexity: O(3*C)
Space complexity: O(2*C)
```

---

### Test Cases

The following test cases have been created to test base and corner use cases:

1. Encode/Decode example sentence "The bird is the word"
2. Encode/Decode larger string (Lorem ipsum of 200 word length) as input
3. Encode/Decode array of random integers as input
4. Encode/Decode array of strings as input
5. Encode/Decode dictionary as input
6. Encode/Decode with null as input

Running the tests can be executed using the following command:

```
python -m unittest HuffmanCoder.py
```