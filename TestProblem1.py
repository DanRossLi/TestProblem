import pandas as pd
import io
import argparse

parser=argparse.ArgumentParser('csv')
parser.add_argument('csv', help="Specify CSV file to take data from")

def ttlResale(csv):
    data = pd.read_csv(csv)
    total = 0
    df = pd.DataFrame(data)
    print(df)
    df['Resale Value'] = pd.to_numeric(df['Resale Value'].replace('[^0-9\.]', '', regex=True)).astype(float)
    total = df['Resale Value'].sum()
    currency = "${:,.2f}".format(total)
    print("Total Resale Value:" +currency)
 
if __name__ == "__main__":       
    args = parser.parse_args()
    ttlResale(args.csv)