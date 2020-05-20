import numpy as np
from PIL import Image
import heapq
import os

from hashlib import sha1
from numpy import all, array, uint8


class hashable(object):
    def __init__(self, wrapped, tight=False):
        self.__tight = tight
        self.__wrapped = array(wrapped) if tight else wrapped
        self.__hash = int(sha1(wrapped.view(uint8)).hexdigest(), 16)

    def __eq__(self, other):
        return all(self.__wrapped == other.__wrapped)

    def __hash__(self):
        return self.__hash

    def unwrap(self):
        if self.__tight:
            return array(self.__wrapped)

        return self.__wrapped



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
        if (self.img_array.shape[2] != 3):
            print(self.img_array.shape)
            print('File is not an acceptable rgb image.')
            exit(0)

        # Structures
        self.heap = []
        self.encodded = {}




    ## Functions for running tests
    def test_img(self,filename):
        self.degredation()
        self.fill_freq_dict()
        img = Image.fromarray(self.img_array)
        if filename.endswith('.jpg'):
            new_filename = filename[:len(filename)-4]+'_degredated.jpg'
            img.save('../images/export/' + new_filename)
        else:
            img.save('../images/export/testrgb.jpg')




    ## Compression functions

    # Increase the frequency of colors / image loss
    def degredation(self):

        # Precision variables
        # (MAYBE: make precision variables a function of the size of the image)
        reso_size = 10
        num_diff_vals = 10


        total_num_colors = num_diff_vals^3
        prec_size = 255.0 / num_diff_vals
        remaining_rows = self.rows % reso_size


        # Set the color of each (reso_size x 1) colomn to average color of that colomn
        # Truncate the values by integer division
        for i in range(0,self.rows-remaining_rows,reso_size):

            for j in range(0,self.colomns):
                valRed = np.array([self.img_array[k][j][0] for k in range(i,i+reso_size)])
                avgRed = valRed.mean()

                valGreen = np.array([self.img_array[k][j][1] for k in range(i,i+reso_size)])
                avgGreen = valGreen.mean()

                valBlue = np.array([self.img_array[k][j][2] for k in range(i,i+reso_size)])
                avgBlue = valBlue.mean()

                avgRGB = [avgRed,avgGreen,avgBlue]
                avgRGB[:] = [int(x) - int(x)%prec_size for x in avgRGB]
                # print(avgRGB,i,j)

                for l in range(i,i+reso_size):
                    self.img_array[l][j] = avgRGB

        # If any rows are left at bottom of image, then finish
        if (remaining_rows != 0):

            for j in range(0,self.colomns):
                valRed = np.array([self.img_array[k][j][0] for k in range(i,self.rows)])
                avgRed = valRed.mean()

                valGreen = np.array([self.img_array[k][j][1] for k in range(i,self.rows)])
                avgGreen = valGreen.mean()

                valBlue = np.array([self.img_array[k][j][2] for k in range(i,self.rows)])
                avgBlue = valBlue.mean()

                avgRGB = [avgRed,avgGreen,avgBlue]
                avgRGB[:] = [int(x) - (x)%prec_size for x in avgRGB]

                for l in range(i,self.rows):
                    self.img_array[l][j] = avgRGB




    def fill_freq_dict(self):
        frequency = {}

        for i in range(0,self.rows):
            pixels = self.img_array[i]

            for j in range(0,self.colomns):
                rgb_val = pixels[j]

                key = hashable(rgb_val)
                if key not in frequency:
                    frequency[key] = 0

                frequency[key] += 1

        # print(len(frequency))

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



    ## Decompression

    def decompress(self,path):
            pass
