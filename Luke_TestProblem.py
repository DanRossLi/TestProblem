import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', help = 'specify filepath')

def main():
    #args = parser.parse_args()
    df = pd.read_csv('TestData.csv')
    df_melt = df.melt(id_vars = ['Item'], value_vars = ['Resale Value'])
    df_melt = df_melt.dropna()
    df_melt['value'] = df_melt['value'].apply(lambda x: x.replace('$','')).apply(lambda x: x.replace(',','')).astype(float)
    df_melt = df_melt.sort_values(by=['Item'])

    totalResale =  df_melt['value'].sum()
    totalFile = open('TotalResaleSummary.txt', 'w')
    totalFile.write('The measured total resale value for this data set is: $' + np.around(totalResale,2).astype(str))    
     
    itemTypes = df_melt['Item'].drop_duplicates()

    byItem = open('TotalResaleByItem.txt','w')
    for item in itemTypes:
        tempList = []
        for ind in df_melt.index:
            if item == df_melt['Item'][ind]:
                tempList.append(df_melt['value'][ind])
        byItem.write('Total Resale Value by item ' + item + ': $' + np.around(sum(tempList),2).astype(str) + '\n')

if __name__ == "__main__":
    main()

    
    
    
    
    
    
    

