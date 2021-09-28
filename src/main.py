import pandas as pd
from collections import Counter
from datetime import timedelta, date,datetime
import numpy as np
import json
import argparse
from urllib.parse import unquote

def create_argument_parser():
    parser  = argparse.ArgumentParser(description = 'head-tail: Grabs N head or tail rows from a text file.')
    parser.add_argument('--input-file', nargs = '?', required = True, help = 'The path of the input file.')
    return parser


if __name__ == "__main__":
    # add command line arguments to send
    parser  = argparse.ArgumentParser(description = 'head-tail: Grabs N head or tail rows from a text file.')
    args = parser.parse_args()

    print(args.input_file)
