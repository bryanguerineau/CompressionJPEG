import numpy as np


def ycrcb_convert(image: np.ndarray) -> np.ndarray:
    '''
    Y = 0.299R + 0.587G + 0.114B
    Cb = −0.1687R − 0.3313G + 0.5B + 128
    Cr = 0.5R − 0.4187G − 0.0813B + 128
    '''
    bwImage = np.empty(np.shape(image))
    for i in range(len(image)):
        for j in range(len(image)):
            R = image[i][j][0]
            G = image[i][j][1]
            B = image[i][j][2]
            Y = 0.299 * R + 0.587 * G + 0.114 * B
            Cb = (-1) * (0.1687 * R) - (0.3313 * G) + 0.5 * B + 128
            Cr = (0.5 * R) - (0.4187 * G) - (0.0813 * B) + 128
            YCbCr = [Y, Cb, Cr]
            bwImage[i][j] = YCbCr
    return bwImage


def bw_convert(image: np.ndarray) -> np.ndarray:
    '''
    Grayscale = (R + G + B ) / 3
    '''
    bwImage = np.empty(np.shape(image))
    for i in range(len(image)):
        for j in range(len(image)):
            R = image[i][j][0]
            G = image[i][j][1]
            B = image[i][j][2]
            Grayscale = 0.299 * R + 0.587 * G + 0.114 * B
            bwImage[i][j] = Grayscale
    return bwImage