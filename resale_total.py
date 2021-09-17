import pandas as pd 
# -------------------CLEANING THE DATA
data = pd.read_csv("TestData.csv", delimiter=",") #Removes duplicate entries from the csv file
data = data.drop_duplicates() 
data.to_csv("TestData.csv", index=False)
data["Resale Value"] = data["Resale Value"].str.replace('$','').str.replace(',','').astype(float) #remove format from # values used in calc
data['Resale Difference'] = data['Resale Difference'].str.replace('$','').str.replace(',','').astype(float)
# -------------------WORKING THE DATA
total = data["Resale Value"].sum() #sums total resale values 
with open('TotalResale.txt', 'w') as f: #outputs the total resale value answer in a .txt file
    f.write(str(total))
dataItems = data[["Item", "Resale Value"]].groupby(["Item"]).sum() #sums the resale values by item here into it's own table
with open('ResalebyItem.txt', 'w') as f: #outputs the resale sums by item to a .txt table
    f.write(str(dataItems))
# ------------------DISPLAYING DATA SUMMARY
print("\nData Summary\nTotal Quantity Sold: ", data['Qty'].sum(), "\nTotal Resale Value: ", total, "\nTotal Resale Profit: ", data['Resale Difference'].sum(), "\nTotal Resale Value per Item:\n\n", dataItems)