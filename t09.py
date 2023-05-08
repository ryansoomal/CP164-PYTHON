"""
-------------------------------------------------------
[t09]
-------------------------------------------------------
Author:  Ryan Soomal
ID:      210370340
Email:   soom0340@mylaurier.ca
__updated__ = "2021-01-14"
-------------------------------------------------------
"""
from functions import dsmvwl
def main():
    s = input("Enter a sentence: ")
    out = dsmvwl(s)
    print("Disemvowelled: {}".format(out))
main()