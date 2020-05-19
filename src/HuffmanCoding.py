import numpy as np
from PIL import Image
import heapq
import os

class HeapNode:

    # Object constructor
    def __init__(self, freq, *rgb_vals):

        # Object variables
        self.rgb_vals = np.array(rgb_vals)
        self.freq = freq
        self.left = None
        self.right = None


    # Public functions
    def __cmp__(self, other):
            if(other == None):
                return -1
            if(not isinstence(other,HeapNode)):
                return -1
            else:
                return self.freq > other.freq



class Huffman:

    # Constructor
    def __init__(self,path):

        self.path = path
        self.img_array = np.array(Image.open(self.path))

        # Shape of rgb image is (rows,colomns,3)
        self.rows = self.img_array.shape[0]
        self.colomns = self.img_array.shape[1]

        #
        self.heap = []
        self.encodded = {}




    # Compression functions

    # Increase the frequency of colors / image loss
    def increase_freq(self):
        # Take each nxn pixels
        # Set the color of each colomn to average color of the colomn
        # Truncate the values by integer division


        # an_array = np.array([[1,2],[3,4]])
        # another_array = np.array([[1,2],[3,4]])
        #
        # comparison = an_array == another_array
        # equal_arrays = comparison.all()
        #
        # print(equal_arrays)
        # OUTPUT
        # True


        block_size = 8

        num_diff_vals = 9
        num_of_colors = num_diff_vals^3
        prec_size = 255.0 / num_diff_vals

        for i in range(0,self.rows,block_size):

            for j in range(0,self.colmns):

                avgRed = self.img_array[i:i+block_size][j][0].mean(axis=0)
                self.img_array[i:i+block_size][j][0] = avgRed

                avgGreen = self.img_array[i:i+block_size][j][1].mean(axis=0)
                self.img_array[i:i+block_size][j][1] = avgGreen

                avgBlue = self.img_array[i:i+block_size][j][2].mean(axis=0)
                self.img_array[i:i+block_size][j][2] = avgBlue
        


    def fill_freq_dict(self,):

        frequency = {}

        for line in self.img_array:

            pixels = self.img_array[line]
            for rgb_val in pixles:

                if not rgb_val in pixles:
                    frequency[rgb_vals] = 0

                frequency[rgb_val] += 1

        return frequency



	def make_heap(self, frequency):
		for key in frequency:
			node = HeapNode(key, frequency[key])
			heapq.heappush(self.heap, node)

	def merge_nodes(self):
            pass

	def create_code(self):
            pass

    def create_codebook(self):
            pass

    def compress(self):
            pass

    # Decompression

    def decompress(self,path):
        # img = Image.fromarray(self.img_array)
        # img.save('../images/export/testrgb.jpg')
            pass
