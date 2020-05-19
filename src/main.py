import numpy as np
from PIL import Image
from Huffman import Huffman


def main():

    input_path = '../images/mountains.jpg'
    h = huffman_alg(userPath)
    output_path = h.compress()

    img = Image.fromarray(img_array)
    img.save('../images/export/testrgb.jpg')

main()
