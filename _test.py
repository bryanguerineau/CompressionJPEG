import sys
from functions.zigzag import count_symbols
from functions.color_convert import bw_convert, ycrcb_convert
from functions.base import load_from_url, imshow



import sys, getopt

def main(argv):
   if argv == 1 :
       url = "http://www.lenna.org/len_std.jpg"
       imgOriginal = load_from_url(url)
       '''
       Dans cette partie, nous testons la fonction cout_sympbols. Elle doit nous renvoyer un dictionnaire avec les symboles et 
       leurs nombre d'itaration dans la liste
       '''
       ycrcbImage = ycrcb_convert(imgOriginal)
       bwImage = bw_convert(imgOriginal)
       imshow(ycrcbImage)
       imshow(bwImage)

if __name__ == "__main__":
   main(sys.argv[1])


