"""
This program assumes a user enters in one file at a time and wants the data
stored such that it is associated with the file it was in. If I wanted to
parse many files entered in the commandline I could do something like:
import sys
for file in sys.args[1:]
    # the code I have written
I would still have to validate for file existence in this way of answering the
prompt. Pandas was also used for the other files in the repo so I am not adding
any new dependencies in this file.
"""

import argparse
import pandas as pd
import collections

parser = argparse.ArgumentParser()
parser.add_argument("file", help="specify path to CSV file")


def find_total_resale_value(df: pd.DataFrame) -> tuple[float, dict]:
    total = 0.0
    item_resale_dict = collections.defaultdict(float)
    for a, b in zip(df["Item"], df["Resale Value"]):
        b_num = float(b[1:].replace(",", ""))
        item_resale_dict[a] += b_num
        total += b_num
    return round(total, 2), item_resale_dict


def make_total_file(totals: list[float], files: list[str]) -> None:
    with open('totalResaleValue.csv', 'w') as f:
        f.write("File Name,Total Resale Value\n")
        for file, total in zip(files, totals):
            f.write("{},${}\n".format(file, total))


def make_item_total_file(item_totals: list[dict], files: list[str]) -> None:
    with open('resalePerItem.csv', 'w') as f:
        f.write("File Name,Item, Item Resale Value\n")
        for file, item_total in zip(files, item_totals):
            for k, v in item_total.items():
                f.write("{},{},${}\n".format(file, k, round(v, 2)))


def main():
    args = parser.parse_args()
    file_name = args.file
    file_names, totals, dicts = [], [], []
    while file_name != 'q':
        try:
            df = pd.read_csv(file_name)
        except FileNotFoundError:
            print("Invalid File Name, Writing Analysis to Files")
            break
        total_resale, item_resale = find_total_resale_value(df)
        file_names.append(file_name)
        totals.append(total_resale)
        dicts.append(item_resale)
        file_name = input("Enter path to next CSV or 'q' to quit: ")
    make_total_file(totals, file_names)
    make_item_total_file(dicts, file_names)


if __name__ == "__main__":
    main()
