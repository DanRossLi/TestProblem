import csv
import pandas as pd


#total = data.groupby('Item')['Resale Value'].sum()

def total_resale_by_group():
    data = pd.read_csv("https://raw.githubusercontent.com/DanRossLi/TestProblem/main/TestData.csv")
    data = pd.DataFrame(data, columns=['Item', 'Resale Value'])
    data['Resale Value'] = data['Resale Value'].str.replace('$','', regex=True).replace(',', '', regex=True).astype('double')
    data_group = data.groupby('Item')['Resale Value'].sum()
    print(data_group)

    #data_float = data['Resale Value'].str.replace('$','', regex=True).replace(',', '', regex=True).astype('double').groupby('Item')['Resale Value']
    #data_group = sum(data_float)
    #print('Total Price of Resale is: $', data_group)


if __name__ == '__main__':
    total_resale_by_group()