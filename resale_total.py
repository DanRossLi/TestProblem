import pandas as pd
#tried to keep things as compact as possible once i finally got the packages to work!

data = pd.read_csv("TestData.csv", delimiter=",")
data["Resale Difference"] = data["Resale Difference"].str.replace('$','').str.replace(',','').astype(float)
#removing the formatting $ signs and commas to make summing easier

total = data["Resale Difference"].sum() #sums total resale values here

with open('TotalResale.txt', 'w') as f: #outputs a file with our total resale value
    f.write(str(total))

dataItems = data[["Item", "Resale Difference"]].groupby(["Item"]).sum() #sums the resale values by item here into it's own table

with open('ResalebyItem.txt', 'w') as f: #creates answer file to show resale totals by item
    f.write(str(dataItems))