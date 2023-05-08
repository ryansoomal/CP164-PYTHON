"""
-------------------------------------------------------
[t10]
-------------------------------------------------------
Author:  Ryan Soomal
ID:      210370340
Email:   soom0340@mylaurier.ca
__updated__ = "2021-01-14"
-------------------------------------------------------
"""
from functions import pig_latin
def main():
    word = input("Word: ")
    out = pig_latin(word)
    print("Pig-Latin: {}".format(out))
    
main()