import pandas as pd #tried to keep things as compact as possible once i finally got the packages to work!

# -------------------CLEANING THE DATA

#Removes duplicate entries from the csv file
data = pd.read_csv("TestData.csv", delimiter=",")
data = data.drop_duplicates() 
data.to_csv("TestData.csv", index=False)

# -------------------WORKING THE DATA
#this section is for finding the specific answers and outputting them to files, as requested/suggested by the README.md

data["Resale Value"] = data["Resale Value"].str.replace('$','').str.replace(',','').astype(float)
#removing the formatting $ signs and commas to make summing easier

total = data["Resale Value"].sum() #sums total resale values 

with open('TotalResale.txt', 'w') as f: 
    f.write(str(total))

dataItems = data[["Item", "Resale Value"]].groupby(["Item"]).sum() #sums the resale values by item here into it's own table

with open('ResalebyItem.txt', 'w') as f: 
    f.write(str(dataItems))

# ------------------DISPLAYING DATA SUMMARY

data['Resale Difference'] = data['Resale Difference'].str.replace('$','').str.replace(',','').astype(float)
totaldiff = data['Resale Difference'].sum()
print("\nData Summary\nTotal Sales: ", data['Qty'].sum(), "\nTotal Resale Value: ", total, "\nTotal Resale Profit: ", totaldiff)