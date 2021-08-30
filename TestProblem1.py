import pandas as pd
import io
import argparse

parser=argparse.ArgumentParser('csv')
parser.add_argument('csv', help="Specify CSV file to take data from")

def ttlResale(csv):
    #These Need to be here, 
    #when pulling from the CSV file,
    #you need to initialize the data frame being used
    csv = pd.read_csv(csv)
    csv['Resale Value'] = pd.to_numeric(csv['Resale Value'].replace('[^0-9\.]', '', regex=True)).astype(float)
    total = csv['Resale Value'].sum()
    currency = "${:,.2f}".format(total)
    print("Total Resale Value:" +currency)
 
if __name__ == "__main__":       
    args = parser.parse_args()
    ttlResale(args.csv)