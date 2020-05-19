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
        self.heap = []
        self.encodded = {}



    # Compression functions

    def increase_freq(self):
        pass

    def fill_freq_dict(self,img_array):
        pass

	def make_heap(self, frequency):
        pass

	def merge_nodes(self):
        pass

	def create_code(self):
        pass

	def compress(self):
        pass


    # Decompression functions

    def decompress(self):
        pass
