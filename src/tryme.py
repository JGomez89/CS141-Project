import numpy as np
from PIL import Image
from HuffmanCoding import Huffman


def main():

    # Enter whatever .jpg file from images folder
    # Expect degredated image in exported

    filename = 'dog.jpeg'

    path = '../images/' + filename
    h = Huffman(path)
    h.test_img(filename)

main()