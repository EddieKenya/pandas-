import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# print(df)
# print(df.head(3)) prints first 3 rows
# print(df.tail(3)) prints last three rows
# df = pd.read_excel('pokemon_data.xlsx') if excel file
# print(df.columns) read columns
print(df.sort_values('Name'))

# iterating through rows

# for index, row in df.iterrows():
#     if row['Type 1'] == 'Fire':
#         print(index, row)



