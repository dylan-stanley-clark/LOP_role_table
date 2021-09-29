import pandas as pd
from collections import Counter
from datetime import timedelta, date,datetime
import numpy as np
import json
import argparse
import os
# pre-proccesing script to clean up lop role table downloaded as xlsx

def create_argument_parser():
    """
    Function to add command line arguments at run time
    """
    parser  = argparse.ArgumentParser(description = 'head-tail: Grabs N head or tail rows from a text file.')
    parser.add_argument('--input-file', nargs = '?', required = False, help = 'The path of the input file.')
    return parser


if __name__ == "__main__":
    # add command line arguments to send
    parser  = argparse.ArgumentParser(description = 'Script to proccess LOP role table')
    args = parser.parse_args()
    aws_key = os.environ['aws_key']
    #print(args.input_file)
    print(aws_key,"Some other stuff too and more")
