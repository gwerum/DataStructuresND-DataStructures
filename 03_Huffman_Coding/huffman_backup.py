import sys
import numpy as np

import pdb

################ Encoding ################ 

def huffman_encodes(data):
    assert(type(data) == str)
    probability_distribution = getProbabilityDistribution(data)
    huffman_codes = getHuffmanCodesFrom(probability_distribution)
    encoded_data = encodeData(data, huffman_codes)
    huffman_tree = getHuffmanTreeFrom(huffman_codes)
    return encoded_data, huffman_tree

def getProbabilityDistribution(string):
    probability_distribution = {}
    number_of_chars = len(string)
    for char in set(string):
        probability_distribution[char] = string.count(char)/number_of_chars
    assert(np.isclose(sum(probability_distribution.values()), 1.0, atol=1e-5))
    return probability_distribution

def getHuffmanCodesFrom(distribution):
    # Base case for distribution with 2 chars only
    if(len(distribution) == 2):
        return dict(zip(distribution.keys(), ['0', '1']))

    # Create a new distribution by merging lowest probability pair of chars
    new_distribution = distribution.copy()
    char1, char2 = getLowestProbabilityCharsFrom(distribution)
    prob1, prob2 = new_distribution.pop(char1), new_distribution.pop(char2)
    new_distribution[char1 + char2] = prob1 + prob2

    # Recurse and compute Huffman codes on new distribution
    codes = getHuffmanCodesFrom(new_distribution)
    code_char1_char2 = codes.pop(char1 + char2)
    codes[char1], codes[char2] = code_char1_char2 + '0', code_char1_char2 + '1'

    return codes

def getLowestProbabilityCharsFrom(distribution):
    assert(len(distribution) >= 2) # Min distribution length = 2
    sorted_distribution = sorted(distribution.items(), key=lambda x: x[1])
    return sorted_distribution[0][0], sorted_distribution[1][0]

def encodeData(data, huffman_codes):
    encoded_data = ''
    for char in data:
        encoded_data += huffman_codes[char]
    return encoded_data

def getHuffmanTreeFrom(huffman_codes):
    huffman_tree = {}
    for char in huffman_codes:
        huffman_tree[huffman_codes[char]] = char
    return huffman_tree

################ Decoding ################ 

def huffman_decodes(data, tree):
    decoded_data = ''
    tree_depths = max([len(key) for key in tree.keys()])
    while data:
        char, data = decodeData(data, tree, tree_depths)
        decoded_data += char
    return decoded_data

def decodeData(data, tree, tree_depths):
    data_section = data[:(tree_depths+1)]
    char, code_length = getNextCharacter(data_section, tree)
    data = data[code_length:]
    return char, data

def getNextCharacter(code, tree):
    while code:
        if code in tree:
            return tree[code], len(code)
        else:
            return getNextCharacter(code[:-1], tree)

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    a_great_sentence = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet,"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encodes(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decodes(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    assert(a_great_sentence == decoded_data)
