import numpy as np
from PIL import Image
from Huffman import huffman_alg




# Take string or image as input

    # Create array representation of rgb_image
# img = Image.open('../images/mountains.jpg')
# img_array = np.array(img)
# print(img_array.shape)      # (170, 256, 3)


## Image -> Binary
# Hash similar valued pixels to same color (decrease resolution)
    # idk: "truncate" rgb values
    # (or) make 3x3 pixel set be represented by the middle pixel

# Huffman Algorithm


    # Make frequency dictionary
    # Make heap
    # Merge Nodes and build tree
    # Make codes
    # Encode pixels
    # Pad encodded text
    # Make byte array
# Output the byte array to binary file
    # Maybe: show improvement by comparing it to a naive conversion from image to binary


## Binary-> Image
# img = Image.fromarray(img_array)
# print(img_array)
# img.save('../images/export/testrgb.jpg')
