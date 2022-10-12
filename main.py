import pandas as pd

df = pd.read_csv('C:/Users/paulg/Documents/Coding/Witzig/CSV to Excel/iss_data.csv')
print(df)
df.to_excel(r'C:/Users/paulg/Documents/Coding/Witzig/CSV to Excel/iss_data.xlsx', index = None, header=True)