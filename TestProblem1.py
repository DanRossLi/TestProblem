
import pandas as pd





def total_resale():
    data = pd.read_csv("https://raw.githubusercontent.com/DanRossLi/TestProblem/main/TestData.csv")
    data_float = data['Resale Value'].str.replace('$','', regex=True).replace(',', '', regex=True).astype('double')
    total = data_float.sum()
    print('Total Price of Resale is: $', total)


if __name__ == '__main__':
    total_resale()