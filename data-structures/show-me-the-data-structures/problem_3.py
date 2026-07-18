import heapq


class HuffmanNode:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Count frequency of each character
def calculate_frequencies(data):

    frequency = {}

    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


# Build Huffman Tree
def build_huffman_tree(frequency):

    heap = []

    for char in frequency:
        node = HuffmanNode(char, frequency[char])
        heapq.heappush(heap, node)

    if len(heap) == 0:
        return None

    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = HuffmanNode(None, left.freq + right.freq)

        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    return heap[0]


# Generate Huffman Codes
def generate_huffman_codes(node, code, huffman_codes):

    if node is None:
        return

    if node.char is not None:

        if code == "":
            huffman_codes[node.char] = "0"
        else:
            huffman_codes[node.char] = code

        return

    generate_huffman_codes(node.left, code + "0", huffman_codes)
    generate_huffman_codes(node.right, code + "1", huffman_codes)


# Encode the string
def huffman_encoding(data):

    if data == "":
        return "", None

    frequency = calculate_frequencies(data)

    tree = build_huffman_tree(frequency)

    huffman_codes = {}

    generate_huffman_codes(tree, "", huffman_codes)

    encoded_data = ""

    for char in data:
        encoded_data = encoded_data + huffman_codes[char]

    return encoded_data, tree


# Decode the string
def huffman_decoding(encoded_data, tree):

    if tree is None:
        return ""

    # Only one unique character
    if tree.left is None and tree.right is None:
        return tree.char * len(encoded_data)

    decoded_data = ""

    current = tree

    for bit in encoded_data:

        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_data = decoded_data + current.char
            current = tree

    return decoded_data


# ---------------- Main ----------------

if __name__ == "__main__":

    # Test Case 1
    print("Test Case 1")

    sentence = "Huffman coding is fun!"

    encoded_data, tree = huffman_encoding(sentence)

    print("Encoded:", encoded_data)

    decoded_data = huffman_decoding(encoded_data, tree)

    print("Decoded:", decoded_data)


    # Test Case 2 (Empty String)
    print("\nTest Case 2")

    sentence = ""

    encoded_data, tree = huffman_encoding(sentence)

    print("Encoded:", encoded_data)

    decoded_data = huffman_decoding(encoded_data, tree)

    print("Decoded:", decoded_data)


    # Test Case 3 (Single Character)
    print("\nTest Case 3")

    sentence = "AAAAAAAAAA"

    encoded_data, tree = huffman_encoding(sentence)

    print("Encoded:", encoded_data)

    decoded_data = huffman_decoding(encoded_data, tree)

    print("Decoded:", decoded_data)