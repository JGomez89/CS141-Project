import numpy as np
from PIL import Image
from HuffmanCoding import Huffman


def main():
    path = '../images/mountains.jpg'
    h = Huffman(path)

    # Compression
    output_path = h.compress()

    # Decompression
    h.decompress(output_path)


main()
