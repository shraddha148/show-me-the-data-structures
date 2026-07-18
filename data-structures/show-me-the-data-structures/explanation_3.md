## Reasoning Behind Decisions:
A frequency dictionary is used to count how many times each character appears in the input string.
A min-heap (priority queue) is used to efficiently build the Huffman Tree by always selecting the two nodes with the smallest frequencies.
The Huffman Tree is traversed recursively to generate a unique binary code for each character.
The original string is encoded by replacing each character with its Huffman code.
To decode, the encoded bits are traversed through the Huffman Tree until a leaf node (character) is reached.
Edge cases such as an empty string and a string containing only one unique character are handled separately.
Time Efficiency:
Calculating character frequencies: O(n), where n is the length of the input string.
Building the Huffman Tree: O(k log k), where k is the number of unique characters.
Generating Huffman codes: O(k).
Encoding the string: O(n).
Decoding the encoded string: O(n).

## Overall Time Complexity: O(n + k log k)

where:

n = length of the input string.
k = number of unique characters.
Space Efficiency:
Frequency dictionary stores k unique characters.
The min-heap and Huffman Tree together store k nodes.
The Huffman code dictionary stores k codes.
The encoded string requires space proportional to its encoded length.

## Overall Space Complexity: O(n + k)

where:

n = length of the encoded/output string.
k = number of unique characters.
