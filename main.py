import numpy as np 
import pandas as pd 
from functions import entropy


print('start')
df = pd.read_csv('C:\\Users\\ASUS\\Desktop\dsFinal\\Decision-Tree\dataset\\feature_test.csv')
print(df.head())

duplicate_rows_data = df[df.duplicated()]
# pak kardn duplicates as dataset
df = df.drop_duplicates()

for column in df.columns:
    num_distinct_values = len(df[column].unique())
    print(f"{column}: {num_distinct_values} distinct values")

print('end')

h = ['m', 'm', 'm', 'f']

print(entropy(h))