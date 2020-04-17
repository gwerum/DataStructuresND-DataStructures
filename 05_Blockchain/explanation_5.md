## Blockchain.py

### Code explanation & Data Structures

The base data structure of a blockchain is a (single) linked list, which can only be traversed from its end (tail) to its source (head). New blocks are always added to its end, the first block of the chain is called genesis block. The difference to a standard linked list is, that it uses hash pointers instead of memory pointers to link to the previous element in the list (previous block in the blockchain). 

Hash pointers are comprised of two parts:

* Pointer to where some information is stored (pointer to memory location of previous block)
* Cryptographic hash of that information (hash of the information stored in the previous block)

So, a hash pointer can not only be used to get the information from the previous block, but also be used to verify that this information hasn't been changed since creation of the block.

![hash_pointers](https://github.com/gwerum/DataStructuresND-DataStructures/05_Blockchain/hash_pointer.jpg "Use of hash pointers in block chain")

Generating the hash of the information not only includes the data stored in the previous block but also the hash pointer of the previous block. This is key to idea of the blockchain. By this it is made sure, that if a single block is changed the whole blockchain following this block will notice. I want go deeper into this, if you're more interested in learning how this works in detail read this enlightning article: 

[Blockchain in 7-steps](https://blog.goodaudience.com/blockchain-for-beginners-what-is-blockchain-519db8c6677a?gi=61da6b19d02)

---

### Runtime efficiency

#### Inititializing & adding new block to blockchain

Let's consider you want to store data of average size D per block, each block then holds the following information:

| Block |
| ------------------- |
| Hash pointer P |
| Timestamp T |
| Data D |
| Hash H |

Hash pointer P, timestamp T and hash H are independ of size of data D and in general smaller than D. For simplicity we can say the total memory required for each block is of size D.
During initialization of a block not only P, T, D and H need to be written (which can be assumed to be in constant time O(1)), also the hash code H needs to be computed. Computing a hash code for a string object is typically of order O(n) since its computation is of the following form where `s[i]` is the i-th character of the string:
```
s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1]
```
**Note**: In reality, the time complexity for computing the hash is not so much influenced by the size of the data D stored in the block, but by the requirements towards the generated hash (e.g. a bitcoin hash needs to start with 19 zeros). The time complexity in this case is a function of computational power and luck.

Thus, the following complexities can be estimated for creating a blockchain with a total number of B blocks.

|  | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| Initializing new block | O(D + 1) | |
| Chaining all blocks | O(B) | O(B*D) |
| **Total** | **O(B + D + 1) ~ O(B + D)** | **O(B\*D)** |

**D**: Size of data stored per block
**B**: Number of blocks in blockchain

---

### Test Cases

The following test cases have been created to test base and corner use cases:

1. Create blockchain with 10 blocks each storing one word as data
2. Create blockchain with dictionary as data
3. Create large blockchain with 10.000 blocks 
4. Alter data of single block and check if detected

Running the tests can be executed using the following command:

```
python -m unittest Blockchain.py
```