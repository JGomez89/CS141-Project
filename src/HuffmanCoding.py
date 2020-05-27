import numpy as np
from PIL import Image
import heapq
import os



class HeapNode:

    # Object constructor
    def __init__(self, freq, rgb_vals):

        # Object variables
        # self.rgb_vals = np.asarray(rgb_vals)
        self.rgb_vals = rgb_vals
        self.freq = freq
        self.left = None
        self.right = None


    # Public functions
    def __cmp__(self, other):
            if(other == None):
                return -1
            if(not isinstance(other,HeapNode)):
                return -1
            else:
                return self.freq > other.freq




class Huffman:

    # Constructor
    def __init__(self,path):

        self.path = path
        self.img_array = np.array(Image.open(self.path))

        # Shape of rgb image is (rows,columns,3)
        self.rows = self.img_array.shape[0]
        self.columns = self.img_array.shape[1]
        if (self.img_array.shape[2] != 3):
            print(self.img_array.shape)
            print('File is not an acceptable rgb image.')
            exit(0)

        # Structures
        self.heap = []
        self.encodded = {}




    ## Functions for running tests
    def test_img(self,filename):


        self.compress()

        root = self.decode_codebook()
        self.print_tree(root)
                

        # print 'Number of colors in image:',len(freq)

        img = Image.fromarray(self.img_array)
        if filename.endswith('.jpg'):
            new_filename = filename[:len(filename)-4]+'_degredated.jpg'
            img.save('../images/export/' + new_filename)
        else:
            img.save('../images/export/testrgb.jpg')


    def print_tree(self,root,code=''):

        if(isinstance(root.left,HeapNode) or isinstance(root.right,HeapNode)):

            leftChild = root.left
            rightChild = root.right

            if(root.left != None):
                code1 = code +'0'
                self.print_tree(leftChild,code1)

            if(root.right != None):
                code2 = code + '1'
                self.print_tree(rightChild,code2)

            return

        print ('Reached rgb_val: ', root.rgb_vals)
        print(code)






    ## Compression functions

    # Increase the frequency of colors / image loss
    def degredation(self):

        # Precision variables
        # (MAYBE: make precision variables a function of the size of the image)
        reso_size = self.rows/120
        num_diff_vals = 10


        total_num_colors = (num_diff_vals+1)^3
        prec_size = 255.0 / num_diff_vals
        remaining_rows = self.rows % reso_size


        # Set the color of each (reso_size x 1) colomn to average color of that colomn
        # Truncate the values by integer division
        for i in range(0,self.rows-remaining_rows,reso_size):

            for j in range(0,self.columns):
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

            for j in range(0,self.columns):
                valRed = np.array([self.img_array[k][j][0] for k in range(i,self.rows)])
                avgRed = valRed.mean()

                valGreen = np.array([self.img_array[k][j][1] for k in range(i,self.rows)])
                avgGreen = valGreen.mean()

                valBlue = np.array([self.img_array[k][j][2] for k in range(i,self.rows)])
                avgBlue = valBlue.mean()

                avgRGB = [avgRed,avgGreen,avgBlue]
                avgRGB[:] = [int(x) - int(x)%prec_size for x in avgRGB]

                for l in range(i,self.rows):
                    self.img_array[l][j] = avgRGB



    def fill_freq_dict(self):

        frequency = {}

        for i in range(0,self.rows):
            pixels = self.img_array[i]

            for j in range(0,self.columns):
                rgb_val = pixels[j]

                key = (rgb_val[0],rgb_val[1],rgb_val[2])
                if (key not in frequency):
                    frequency[key] = 0

                frequency[key] += 1

        return frequency



    def make_heap(self, frequency):

        for key in frequency:
            node = HeapNode(frequency[key],key)
            heapq.heappush(self.heap, node)



    def merge_nodes(self):
        while(len(self.heap)>1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			merged = HeapNode(node1.freq + node2.freq, None)
			merged.left = node1
			merged.right = node2

			heapq.heappush(self.heap, merged)



    def create_codebook(self):
            pass


    def create_code(self):
            pass


    def compress(self):
        self.degredation()
        self.make_heap(self.fill_freq_dict())
        self.merge_nodes()
        self.create_codebook()
        self.create_code()






    ## Decompression

    def decode_codebook(self):
        root = HeapNode(None,None)

        # Read from txtFile file to get code and rgb_vals
        #Testing
        codes = ('0110100','0110101','000','001')
        rgb_vals = ((15,100,200),(135,20,0),(45,45,45),(0,0,100))

        self.tree_insert(root,codes[0],0,rgb_vals[0])
        self.tree_insert(root,codes[1],0,rgb_vals[1])
        self.tree_insert(root,codes[2],0,rgb_vals[2])
        self.tree_insert(root,codes[3],0,rgb_vals[3])

        return root



    def tree_insert(self,root,code,index,rgb_vals):
        if (len(code) == index):
            root.rgb_vals = rgb_vals

        else:
            if(code[index] == '0'):
                if(not isinstance(root.left,HeapNode)):
                    root.left = HeapNode(None,None)

                self.tree_insert(root.left,code,index+1,rgb_vals)


            elif(code[index] == '1'):
                if(not isinstance(root.right,HeapNode)):
                    root.right = HeapNode(None,None)

                self.tree_insert(root.right,code,index+1,rgb_vals)



    def decode_binary(self):
            pass

    def decompress(self):
        root = self.decode_codebook()
        self.print_tree(root)
