import pandas as pd
import numpy as np
import decimal as dc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="specify path to file")


def csv_to_df(filepath):
    csv_file = filepath + '.csv'
    return pd.read_csv(csv_file)


def clean_and_group_df(df):
    # reformat and convert resale value to Decimal
    df['Resale Value'] = df['Resale Value'].str.replace('$', '', regex=False)
    df['Resale Value'] = df['Resale Value'].str.replace(',', '', regex=False)
    df['Resale Value'] = df['Resale Value'].apply(dc.Decimal)

    # creating a pandas groupby object
    grouped = df.groupby(
        'Item').agg({'Resale Value': np.sum})
    grouped.rename(
        columns={'Resale Value': 'Resale Sum By Item'}, inplace=True)
    return grouped


def summary_stats(df):
    totalResale = df['Resale Sum By Item'].sum()
    return ('Total resale value: ' + str(totalResale))


if __name__ == "__main__":
    args = parser.parse_args()
    df = csv_to_df(args.filepath)
    group = clean_and_group_df(df)
    group.to_csv(args.filepath+'_summary.csv')
    summary_file = open(args.filepath+'_summary.txt', 'w')
    summary_file.write(summary_stats(group))
    summary_file.close()
