# For students
# TODO: Write your 'main' code
# convert color image into gray image (or image in YCrCb space)



ycrcbImage = ycrcb_convert(imgOriginal)
bwImage = bw_convert(imgOriginal)
# imshow(bwImage)
# imshow(ycrcbImage)

# This is just an example of coding, you can make your code differently

# ADVICE: create an other 'Code cell' and write/test your code gradually there
# since the code given here is not exectable yet

img = cv2.cvtColor(...)
# color
# First, you can work with only gray images for simplicity


width = len(img[0])
height = len(img)

#
img_gray = np.zeros((height, width), np.float32) + img[:, :, 0]
#

# show img_gray
imshow(img_gray)


# define block size
def blocksize() ->:


# compute number of blocks

# padding

# luminance channels

# for color images -----
# chrominance channels should be sub-sampled with different sub-sampling factors
# A very simple way: using a 2x2 averaging filter # another type of filter can be used
# then we can work with the sub-sampled version...
# --------------------

# define empty matrices to store Dct
# imgDct

# define empty matrices to store the quantized values
# imgQ


# This will be used for of ZigZag...
col = np.array([1, 2, 1, 1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5,
                6, 7, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 6, 7, 8,
                8, 7, 8])

lig = np.array([1, 1, 2, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 1, 2,
                3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 5, 6, 7, 8, 8, 7, 6, 7, 8, 8])

ZZ_Blk = np.zeros(blockSize * blockSize)  # 1D

vRLC = []

size_vRLC = 0

# pseudo-code
for i in range('number of block'):  # of course, this needs to be computed
    for j in range('number of block'):
        block = y[....]).  # extract the block

        # dct
        # you can use something like imgDct['index'] = ...

        # quantification
        # you can use something like imgQ['index'] = ...

        # easy ZigZag Version 2:
        ZZ_Blk = ...
        #
        # zigzag (1D)

        # run length coding (1D)
        # can use `extend` function of numpy vRLC.extend()

        # end for

        # Huffman
        mat_table: dict = construct_huffman_table...
        mat_encoded: str = encode_huffman...