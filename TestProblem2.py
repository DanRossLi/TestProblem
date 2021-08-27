import pandas as pd
import io
import argparse

parser=argparse.ArgumentParser('csv')
parser.add_argument('csv', help="Specify CSV file to take data from")

def allResale(csv):
    data = pd.read_csv(csv)
    df = pd.DataFrame(data, columns = ['Item', 'Resale Value'])
    df['Resale Value'] = pd.to_numeric(df['Resale Value'].replace('[^0-9\.]', '', regex=True)).astype(float)
    pd.options.display.float_format = '${:,.2f}'.format
    grouped = df.groupby('Item')['Resale Value'].sum().reset_index()
    print(grouped)

if __name__ == "__main__":       
    args = parser.parse_args()
    allResale(args.csv)