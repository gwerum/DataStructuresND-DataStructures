## Explanations for HuffmanCoder.py

---

### Code explanation & Data Structures

The implementation consists of two classes, the **class HuffmanCoder()** and the **class HuffmanTree()**. 

#### class HuffmanTree()
This class takes as input the probability distribution of unique chars of the input data. I decided to use a simple Python dictionary for storing the Huffman tree. The tree is constructed in a recursive manner. 
To make things simple and ease code readibility in the actual encoding and decoding methods, I decided to have "two" trees, one for encoding and the other for decoding. This doesn't effect much runtime since it only adds time and space complexity of order C (the total number of unique chars, which is generally small compared to the total numbers of chars N of the input).

Here an example of the dictionary tree for the input sentence "The bird is the word":
```
Tree_Encoding = {' ': '110', 'e': '010', 'i': '000', 'r': '001', 'd': '1110', 'h': '1111', 'w': '1010', 'T': '1011', 'o': '1000', 't': '1001', 's': '0110', 'b': '0111'}

Tree_Decoding = {'110': ' ', '010': 'e', '000': 'i', '001': 'r', '1110': 'd', '1111': 'h', '1010': 'w', '1011': 'T', '1000': 'o', '1001': 't', '0110': 's', '0111': 'b'}
```
The tree above is an example for a small tree. Generally, high probability chars get assigned less binary digits and small probability chars get assigned more binary digits. In the example above: 'e' = 010 has higher probability of occurence then 'o' = 1000.

#### class HuffmanCoder()
This class basically takes care of all the rest: the input/output handling, computation of probability distribution of unique chars C and encoding/decoding using the HuffmanTree(). 
In particular, I had to take care that if the input data is not provided in string format I have to convert it first to string format before encoding and convert it back to original format after decoding. For this, I used the json library and its methods *json.dumps()* and *json.loads()*.

---

### Runtime efficiency

#### class HuffmanTree()
Computing the Huffman tree requires one recursion for constructing each tree node. In worst case one tree node for each unique char of the input string will be created (C: total number of unique chars).
During tree construction the temporary tree (worst case size C) needs to be sorted to extract the two lowest probability chars during each recursion.
I decided to generate an additional "decoding tree" to reduce complexity and ease code readability in the decoding method. This adds another order C to space and time complexity.

| class HuffmanTree() | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| Creating tree nodes | O(C) | O(C) |
| Sort temporary tree | O(C) | |
| Creating "decoding" tree | O(C) | O(C) |
| **Total** | **O(3C)** | **O(2C)** |

**C**: total number of unique chars in input string


#### class HuffmanCoder()

The following tasks are performed:

1. Read and store input string of size N (total number of chars)
2. Compute probability distribution of unique chars C (total number of unique chars in N)
3. Encoding data:
* Conversion of each char of input with size N to Huffman Code
* Huffman code lookup for each char from tree on average in constant time
* Encoded data stored with approximately size N/2 (empirical received, exact computation of size more complicated)
4. Decoding data:
* Back-conversion and storage of each char of input with size N
* Huffman tree loopup in constant time, however recursion needed to identify code length. Maximum number of recursions equals tree depths, which is worst case C-1, in average less than C/2 can be assumed since higher probability chars less deep in tree.


| class HuffmanCoder() | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| Reading & storing input data | O(N) | O(N) |
| Computing char distribution | O(C) | |
| Encoding data | O(N) | O(N/2) |
| Decoding data | O(N + N*(C/2)) | O(N) |
| **Total** | **O(3N + N(C/2) + C)** | **O(2.5N)** |

**C**: total number of unique chars in input string
**N**: total number of chars in input string

#### Overall complexity

Considering that generally N >> C the following estimation of overall complexity can be made:

|  | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| class HuffmanTree() | O(3C) | O(2C) |
| class HuffmanCoder() | O(3N + N(C/2) + C) | O(2.5N) |
| **Total** | **O(3N + N(C/2) + 4C) ~ O(N) ** | **O(2.5N + 2C) ~ O(N)** |

**C**: total number of unique chars in input string
**N**: total number of chars in input string

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