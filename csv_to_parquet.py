import pyarrow as pa
import pandas as pd
import pyarrow.csv as pcsv
import pyarrow.parquet as pq
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="specify path to file")

def csv_to_parquet(filepath):
    csv_file = filepath + '.csv'
    parquet_file = filepath + '.parquet'
    csv = pcsv.read_csv(csv_file)
    pq.write_table(csv, where = parquet_file)

def parquet_to_csv(filepath):
    parquet_file = filepath + '.parquet'
    csv_file = filepath + 'New.csv'
    table = pq.read_table(parquet_file)
    pcsv.write_csv(table,csv_file,write_options=pcsv.WriteOptions(include_header=True))
    
def parquet_manipulate(filepath):
    parquet_file = filepath + '.parquet'
    table = pq.read_table(parquet_file)
    df = table.to_pandas()
    #table.group_by("Item").aggregate([("Resale Value","sum")])
    

if __name__ == "__main__":       
    args = parser.parse_args()
    csv_to_parquet(args.filepath)
    #parquet_manipulate(args.filepath)
    #parquet_to_csv(args.filepath)
