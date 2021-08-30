import pandas as pd
import io
import argparse

parser=argparse.ArgumentParser('csv')
parser.add_argument('csv', help="Specify CSV file to take data from")

def allResale(csv):
    csv = pd.read_csv(csv)
    csv['Resale Value'] = pd.to_numeric(csv['Resale Value'].replace('[^0-9\.]', '', regex=True)).astype(float)
    grouped = csv.groupby('Item')['Resale Value'].sum().reset_index()
    print(grouped)

if __name__ == "__main__":       
    args = parser.parse_args()
    allResale(args.csv)