import pandas as pd
import io
import argparse

parser=argparse.ArgumentParser('csv')
parser.add_argument('csv')
args = parser.parse_args()

data = pd.read_csv(args.csv)
total = 0
df = pd.DataFrame(data)
print(df)
df['Resale Value'] = pd.to_numeric(df['Resale Value'].replace('[^0-9\.]', '', regex=True)).astype(float)
total = df['Resale Value'].sum()
currency = "${:,.2f}".format(total)
print("Total Resale Value:" +currency)