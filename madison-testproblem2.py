import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("file_name", help="csv file to read", type=str)
args = parser.parse_args()

df = pd.read_csv(args.file_name)

# Need to change the currency in the table from strings to floats. Changing column name to keep unit information
df.rename(columns={'Resale Value': 'Resale Value ($)', 'Resale Per Ticket' : 'Resale Per Ticket ($)', 'Resale Difference' : 'Resale Difference ($)'}, inplace=True)

# Getting the '$' and ',' out of the strings then converting to float
df['Resale Value ($)'] = df['Resale Value ($)'].str.replace('[,\$]', '', regex=True).astype('float')
df['Resale Per Ticket ($)'] = df['Resale Per Ticket ($)'].str.replace('[,\$]', '', regex=True).astype('float')
df['Resale Difference ($)'] = df['Resale Difference ($)'].str.replace('[,\$]', '', regex=True).astype('float')

# Writing the total resale value to a txt file
file = open('output1.txt', 'w')
file.write('Total Resale Value: $'+'{:,}'.format(df['Resale Value ($)'].sum()))
file.close()

# Grouping by item, getting sum of resale value, creating csv for totals by item
df_grpby_item_sums = df.groupby('Item').sum()
df_grpby_item_sums.rename(columns={'Resale Value ($)':'Total Resale Value ($)'}, inplace=True)
df_grpby_item_sums['Total Resale Value ($)'].to_csv('output2.csv')
