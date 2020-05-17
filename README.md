# CS141-Project

## Members:
Justin Gomez, Christopher Saito, Rizelle Vinluan

## Description:
Program which compress an image by taking that colored image as input and outputting a minimized binary string using greedy algorithm (Huffman Algorithm), which can be read back into its original colored image (however with an expected drop in resolution since we will hash pixels with similar values to the same color, thus increasing color frequency to take advantage of the Huffman Algorithm).


# Goals

## Take string or image as input
 Create array representation of rgb_image

## Image -> Binary
### Hash similar valued pixels to same color (decrease resolution)
idk: "truncate" rgb values
(or) make 3x3 pixel set be represented by the middle pixel

### Huffman Algorithm
    # Make frequency dictionary
    # Make heap
    # Merge Nodes and build tree
    # Make codes
    # Encode pixels
    # Pad encodded text
    # Make byte array
### Output the byte array to binary file
Maybe: show improvement by comparing it to a naive conversion from image to binary


## Binary-> Image
