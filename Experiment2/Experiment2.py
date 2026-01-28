import heapq
from collections import defaultdict


class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

    
    def __lt__(self, other):
        return self.freq < other.freq


def generate_codes(root, code, encode_map, decode_map):
    if root is None:
        return

    if root.left is None and root.right is None:
        encode_map[root.ch] = code
        decode_map[code] = root.ch
        return

    generate_codes(root.left, code + "0", encode_map, decode_map)
    generate_codes(root.right, code + "1", encode_map, decode_map)



def decode(encoded, decode_map):
    curr = ""
    result = ""

    for bit in encoded:
        curr += bit
        if curr in decode_map:
            result += decode_map[curr]
            curr = ""

    return result



def huffman(s):
    
    freq = defaultdict(int)
    for ch in s:
        freq[ch] += 1

    
    heap = []
    for ch, f in freq.items():
        heapq.heappush(heap, Node(ch, f))

    
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        parent = Node('#', a.freq + b.freq)
        parent.left = a
        parent.right = b

        heapq.heappush(heap, parent)

    
    encode_map = {}
    decode_map = {}
    generate_codes(heap[0], "", encode_map, decode_map)

    print("Huffman Codes:")
    for ch, code in encode_map.items():
        print(f"{ch}: {code}")

    
    encoded = ""
    for ch in s:
        encoded += encode_map[ch]

    print("\nEncoded String:", encoded)
    print("Decoded String:", decode(encoded, decode_map))


st = input("Enter the string:\n")
huffman(st)
