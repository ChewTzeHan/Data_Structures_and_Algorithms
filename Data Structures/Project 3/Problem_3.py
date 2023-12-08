import sys
from collections import Counter

class TreeNode(object):
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right
        
    def children(self):
        return self.left, self.right

def Tree_maker(nodes):
    
    while len(nodes) > 1:
        
        (char1, freq1) = nodes[0]
        (char2, freq2) = nodes[1]
        nodes = nodes[2:]
        
        node = TreeNode(char1, char2)
        nodes.append((node, (freq1 + freq2)))
        nodes = sorted(nodes, key=lambda x: x[1])
        
    return nodes[0][0]
    
def Encoder(node, binary_string = ''):
    
    if type(node) is str:
        return {node: binary_string}
     
    (left_node, right_node) = node.children()
    bin_dict = {}
    bin_dict.update(Encoder(left_node, binary_string + '0'))
    bin_dict.update(Encoder(right_node, binary_string + '1'))

    return bin_dict


def huffman_encoding(data):
    
    if type(data) != str:
        data = str(data)
    
    freq = dict(Counter(data))
    freq = sorted(freq.items(), key=lambda x: x[1])
    
    
    root = Tree_maker(freq)
        
    codes = Encoder(root)        

    
    coded_str = ''   
    for i in data:
        coded_str += codes[i]

    return coded_str, root


def huffman_decoding(data,tree):
    
    decoded_str = ''
    root = tree

    
    for i in data:
        
            
        if i == '0':
            tree = tree.left
        elif i == '1':
            tree = tree.right
            
        if type(tree) is str:
            decoded_str += tree
            tree = root
            

    return decoded_str

    


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)


    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values
print('----------------------')
## Test Case 1, EDGE CASE: Usage of special characters

Special_character_sentence = "!#@%&*!@#$*ABC)*>''_$@%"

print ("The size of the data is: {}\n".format(sys.getsizeof(Special_character_sentence)))
print ("The content of the data is: {}\n".format(Special_character_sentence))

encoded_data, tree = huffman_encoding(Special_character_sentence)


print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

'''
Expected output:
    The size of the data is: 72

    The content of the data is: !#@%&*!@#$*ABC)*>''_$@%

    The size of the encoded data is: 36

    The content of the encoded data is: 10111100011110100001001011011110011101000001001000110100100010111111111101011100111101

    The size of the decoded data is: 72

    The content of the encoded data is: !#@%&*!@#$*ABC)*>''_$@%
'''
print('----------------------')
## Test Case 2 EDGE CASE: Very long sentence

long_sentence = "Fractionally distilling severely steam cracked heavy fuel results in carbon, light fuel, naphtha, toluene, benzene, butene, butadiene, propane, propene, ethane , ethylene and methane."

print ("The size of the data is: {}\n".format(sys.getsizeof(long_sentence)))
print ("The content of the data is: {}\n".format(long_sentence))

encoded_data, tree = huffman_encoding(long_sentence)


print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

'''
Expected output:
    The size of the data is: 232

    The content of the data is: Fractionally distilling severely steam cracked heavy fuel results in carbon, light fuel, naphtha, toluene, benzene, butene, butadiene, propane, propene, ethane , ethylene and methane.

    The size of the encoded data is: 128

    The content of the encoded data is: 00110001011110100000010011110000111111110101000100000001011000101110001010100111100100010001110011110010000110101011000100111010111110100000001011010101001110101000101001100000101111010000000011001110000100111110111010100010010000101100101110110110100001110111110010101011010001001010100111110011110110000010101011100011001111111010001110001110000100011101100101100101110110110100001000111111101001011111011001111011010010001110010011110001011011011111100100011000111101111001101011011111100100011000111011010011101111110010001100011101101001101000010111001101111110010001101011101110011101011101011111100100011010111011100111010111101111110010001111010011110110101111110011010001111010011110100001100011011111100111010111100010011001010110100111101101011111100011011

    The size of the decoded data is: 232

    The content of the encoded data is: Fractionally distilling severely steam cracked heavy fuel results in carbon, light fuel, naphtha, toluene, benzene, butene, butadiene, propane, propene, ethane , ethylene and methane.
'''
print('----------------------')
## Test Case 3 EDGE CASE: Non-string value provided

empty_sentence = 20231209

print ("The size of the data is: {}\n".format(sys.getsizeof(empty_sentence)))
print ("The content of the data is: {}\n".format(empty_sentence))

encoded_data, tree = huffman_encoding(empty_sentence)


print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

'''
Expected output:
    The size of the data is: 28

    The content of the data is: 20231209

    The size of the encoded data is: 28

    The content of the encoded data is: 110111100101110100

    The size of the decoded data is: 57

    The content of the encoded data is: 20231209
'''