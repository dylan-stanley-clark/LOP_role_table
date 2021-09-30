import pandas as pd
import numpy as np
import openpyxl
import os
import io
#import s3fs
import boto3
import argparse

# aws_credentials = { "key": os.getenv("aws_access"), "secret": os.getenv("aws_key")}
def test_load_aws():
    bucket = "polemics"
    file = "ParlinfoFederalAreaOfResponsibilitiy.xlsx"

    #df = pd.read_excel(f"s3://{bucket}/{file}", storage_options=aws_credentials)
    AWS_ACCESS_KEY_ID = os.getenv("aws_access")[1:-1]
    AWS_SECRET_ACCESS_KEY = os.getenv("aws_key")[1:-1]
    s3 = boto3.resource(
        service_name='s3',
        region_name='ca-central-1',
        aws_access_key_id=str(AWS_ACCESS_KEY_ID),#AWS_ACCESS_KEY_ID,
        aws_secret_access_key=str(AWS_SECRET_ACCESS_KEY)
    )

    # Load csv file directly into python
    file_obj = s3.Bucket('polemics').Object(file).get()
    foo = pd.read_excel(io.BytesIO(file_obj['Body'].read()))
    print("successful writing of table to csv")

def test_write_aws():
    AWS_ACCESS_KEY_ID = os.getenv("aws_access")[1:-1]
    AWS_SECRET_ACCESS_KEY = os.getenv("aws_key")[1:-1]
    s3 = boto3.resource(
        service_name='s3',
        region_name='ca-central-1',
        aws_access_key_id=str(AWS_ACCESS_KEY_ID),#AWS_ACCESS_KEY_ID,
        aws_secret_access_key=str(AWS_SECRET_ACCESS_KEY)
    )

    df = pd.DataFrame({'A' : []})
    s3.Object('polemics', 'test.csv').put(Body=df.to_csv())
    print("successful writing of table to csv")

def create_argument_parser():
    """
    Function to add command line arguments at run time
    """
    parser  = argparse.ArgumentParser(description = 'Script to test out pipeline')
    parser.add_argument('--test-name', nargs = '?', required = True, help = 'The name of the test to conduct')
    return parser

if __name__ == "__main__":
    # add command line arguments to send
    parser  = create_argument_parser()
    args = parser.parse_args()
    if args.test_name == 'write_aws':
        test_write_aws()
    if args.test_name == 'read_aws':
        test_load_aws()
