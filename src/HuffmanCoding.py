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

        if(not isinstance(root,HeapNode)): return

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


    def create_huffman_tree(self):
        freq_dict = self.fill_freq_dict()
        self.make_heap(freq_dict)
        self.merge_nodes()


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




    def create_binfile(self):
        # Create new .bin file


        ##      Schema:
        ##          [size of codebook][codebook][# of columns][encoded img]

        # Create first half of .bin file
        code_dict = fill_code_dict(self)
        self.create_codebook(code_dict)


        # Create second half of .bin file
        self.create_code()


        # Save .bin file

        output_path = ''

        return output_path


    def fill_code_dict(self):
            pass


    def create_codebook(self,code_dict):
            pass


    def create_code(self):
            pass



    def compress(self):
        self.degredation()
        self.create_huffman_tree()
        output_path = self.create_binfile()

        return output_path





    ## Decompression
    def decode_binfile(self):

        # Decoding first then second half of the .bin file
        self.decode_codebook()
        self.decode_binary()


    def decode_codebook(self):
        # [uint] [(uint, uint, bits)...] = A (a1, a2, a3)...(n1,n2,n3)]
        # where A is the number of total groupings/leaf nodes
            pass


    def reconstruct_tree(self,codebook=None):
        root = HeapNode(None,None)

        for key in codebook:
            self.insert_leaf(root,key,0,codebook[key])

        return root



    def insert_leaf(self,root,code,index,rgb_vals):
        if (len(code) == index):
            root.rgb_vals = rgb_vals

        else:
            if(code[index] == '0'):
                if(not isinstance(root.left,HeapNode)):
                    root.left = HeapNode(None,None)

                self.insert_leaf(root.left,code,index+1,rgb_vals)


            elif(code[index] == '1'):
                if(not isinstance(root.right,HeapNode)):
                    root.right = HeapNode(None,None)

                self.insert_leaf(root.right,code,index+1,rgb_vals)



    def decode_binary(self):
        # [uint] [bits] = B Img, where B is the number of columns
        # use reconstruct_tree to decode the binary encoding of the img
            pass

    def array_to_img(self):
        # use decode_binary and convert into numpy array
        # then turn the numpy array into an img
            pass

    def decompress(self):
            # put everything together
            pass
