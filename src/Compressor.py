import numpy as np
from PIL import Image

img = Image.open('../images/plains.jpeg')
array = np.array(img)
print(array.shape)      # (170, 256, 3)
img = Image.fromarray(array)
print(array)
img.save('../images/export/testrgb.jpeg')


# Take string or image as input
    # Create array representation of rgb_image

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
