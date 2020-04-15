## HuffmanCoder.py

### Code explanation & Data Structures

The implementation consists of two classes, the **class HuffmanCoder()** and the **class HuffmanTree()**. 

#### class HuffmanTree()
This class takes as input the probability distribution of chars of the input data. In the implementation I focused on computing the Huffman codes from the probability distribution of the chars. Constructing the tree data structure I basically "out-sourced" to the Python dictionary, which is a tree under the hood. For better code clarity I use two dictionaries, one for converting to binaries during encoding and one for converting to chars during decoding.

Here an example for input sentence "The bird is the word":
```
Huffman_codes = {' ': '110', 'e': '010', 'i': '000', 'r': '001', 'd': '1110', 'h': '1111', 'w': '1010', 'T': '1011', 'o': '1000', 't': '1001', 's': '0110', 'b': '0111'}

Huffman_tree = {'110': ' ', '010': 'e', '000': 'i', '001': 'r', '1110': 'd', '1111': 'h', '1010': 'w', '1011': 'T', '1000': 'o', '1001': 't', '0110': 's', '0111': 'b'}
```
The tree above is an example for a small tree. Generally, high probability chars get assigned less binary digits and small probability chars get assigned more binary digits. For computing the Huffman codes I used a recursive algorithm, which always identifies the two lowest probability chars of the current probability distribution and creates a new tree node for them. Creating a new tree node means in this case, appending a new binary digit to their Huffman code. With this, step-by-step the Huffman codes are computed, which then are used to create a binary Huffman tree.

#### class HuffmanCoder()
This class basically takes care of all the rest: the input/output handling, computation of probability distribution of chars and encoding/decoding using the *HuffmanTree()*. Especially, I had to take care that if the input data is not provided in string format I had to convert first to string format before encoding and converting it back to original format after decoding. For this, I used the json library and its methods *json.dumps()* and *json.loads()*.


### Runtime efficiency

#### class HuffmanTree()
Computing the Huffman codes requires one recursion for constructing each tree node, which are in worst case one node per char, so number of tree nodes/recursion equals the *total number of different chars C* in the input data.  Additionally, during recursion the temporary tree needs to be sorted to extract the two lowest probability chars. The worst case size of the temporary tree equals again C. Constructing the tree from the codes adds another space and time complexity of order C. So the overall complexities for class HuffmanTree() are:
```
Time complexity: O(3*C)
Space complexity: O(2*C)
```

#### class HuffmanCoder()
##### Space complexity
Starting with the space complexity the following four main data structures are in use:

1. Input data of size N (total number of chars)
2. Char distribution probability of size C (total number of different chars in N)
3. Encoded data stored as binary string of appr. size N/2 (empirical received, exact computation of size more complicated)
4. Decoded data of size N (total number of chars of input data)
```
Total space complexity for HuffmanCoder(): O(2,5N + C) ~ O(N)

Considering that generally N >> C
```

##### Time complexity
For calculating the time complexity the following main steps need to be considered:

1. Computation of probability distribution of chars of input with size N
2. Encoding:
	a. Conversion of each char of input with size N to Huffman Code
	b. Huffman code lookup for each char from tree on average in constant time
3. Decoding:
	a. Back-conversion of each char of input with size N
	b. Huffman tree loopup in constant time, however recursion needed to identify code length. Maximum number of recursions equals tree depths, which is worst case C-1.
```
Total time complexity for HuffmanCoder(): O(3*N + (C-1) + 1) ~ O(N)

Considering that generally N >> C
```
##### Overall time and space complexity
Considering time and space complexity from both classes, HuffmanCoder() and HuffmanTree(), the following can be approximated:

```
Time complexity: O(N + 3*C) ~ O(N)
Space complexity: O(N + 2*C) ~ O(N)

Considering that generally N >> C
```
**N**: total number of chars in input string
**C**: total number of different chars in input strings

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