import sys
import numpy as np

class HuffmanTree():
    """docstring for HuffmanTree"""
    def __init__(self, distribution):
        self.codes = self.computeHuffmanCodesFrom(distribution)
        self.tree, self.depths = self.computeTree()

    def computeTree(self):
        huffman_tree = {}
        for char in self.codes:
            huffman_tree[self.codes[char]] = char
        tree_depths = max([len(key) for key in huffman_tree.keys()])
        return huffman_tree, tree_depths

    def computeHuffmanCodesFrom(self, distribution):
        # Base case for distribution with 2 chars only
        if(len(distribution) == 2):
            return dict(zip(distribution.keys(), ['0', '1']))

        # Create a new distribution by merging lowest probability pair of chars
        new_distribution = distribution.copy()
        char1, char2 = self.getLowestProbabilityCharsFrom(distribution)
        prob1, prob2 = new_distribution.pop(char1), new_distribution.pop(char2)
        new_distribution[char1 + char2] = prob1 + prob2

        # Recurse and compute Huffman codes on new distribution
        huffman_codes = self.computeHuffmanCodesFrom(new_distribution)
        code_char1_char2 = huffman_codes.pop(char1 + char2)
        huffman_codes[char1], huffman_codes[char2] = code_char1_char2 + '0', code_char1_char2 + '1'

        return huffman_codes

    def getLowestProbabilityCharsFrom(self, distribution):
        assert(len(distribution) >= 2) # Min distribution length = 2
        sorted_distribution = sorted(distribution.items(), key=lambda x: x[1])
        return sorted_distribution[0][0], sorted_distribution[1][0]

class HuffmanCoder():
    def __init__(self):
        self.input_string = ''
        self.char_distribution = {}
        self.huffman_tree = None
        self.encoded_data = ''
        self.decoded_data = ''

    def huffman_encodes(self, data):
        self.__clearCoder()
        self.__loadInputString(data)
        self.__computeProbabilityDistributionOfChars()
        self.__computeHuffmanTree()
        self.__encodeInputString()
        return self.encoded_data, self.huffman_tree

    def huffman_decodes(self, data, tree):
        self.__clearCoder()
        self.__loadDataAndHuffmanTree(data, tree)
        self.__decodeData()
        return self.decoded_data

    def __clearCoder(self):
        self.__init__()

    def __loadInputString(self, data):
        assert(type(data) == str)
        self.input_string = data

    def __computeProbabilityDistributionOfChars(self):
        number_of_chars = len(self.input_string)
        for char in set(self.input_string):
            self.char_distribution[char] = self.input_string.count(char)/number_of_chars
        assert(np.isclose(sum(self.char_distribution.values()), 1.0, atol=1e-5))

    def __computeHuffmanTree(self):
        self.huffman_tree = HuffmanTree(self.char_distribution)

    def __encodeInputString(self):
        self.encoded_data = ''
        for char in self.input_string:
            self.encoded_data += self.huffman_tree.codes[char]

    def __loadDataAndHuffmanTree(self, data, tree):
        self.encoded_data = data
        self.huffman_tree = tree

    def __decodeData(self):
        while self.encoded_data:
            char = self.__getNextChar()
            self.decoded_data += char

    def __getNextChar(self):
        binary_code = self.__getNextBinarySection()
        huffman_code = self.__extractHuffmanCodeFrom(binary_code)
        self.__removeFromEncodedData(huffman_code)
        return self.huffman_tree.tree[huffman_code]

    def __getNextBinarySection(self):
        return self.encoded_data[:(self.huffman_tree.depths+1)]

    def __removeFromEncodedData(self, huffman_code):
        self.encoded_data = self.encoded_data[len(huffman_code):]

    def __extractHuffmanCodeFrom(self, binary_code):
        while binary_code:
            if binary_code in self.huffman_tree.tree:
                return binary_code
            else:
                return self.__extractHuffmanCodeFrom(binary_code[:-1])

if __name__ == "__main__":
    coder = HuffmanCoder()

    a_great_sentence = "The bird is the word"

    a_great_sentence = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet,"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = coder.huffman_encodes(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = coder.huffman_decodes(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    assert(a_great_sentence == decoded_data)
