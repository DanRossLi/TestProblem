import pandas as pd
import requests
import io

url = "https://raw.githubusercontent.com/TheRealSeat/TestProblem/main/TestData.csv?token=AS6K546XAD4DBV44RTXRFODBF6A7E"
download = requests.get(url).content

data = pd.read_csv(io.StringIO(download.decode('utf-8')))
df = pd.DataFrame(data, columns = ['Item', 'Resale Value'])
df['Resale Value'] = pd.to_numeric(df['Resale Value'].replace('[^0-9\.]', '', regex=True)).astype(float)
pd.options.display.float_format = '${:,.2f}'.format
grouped = df.groupby('Item')['Resale Value'].sum().reset_index()
print(grouped)