
import pandas as pd
df = pd.read_csv('dataset2.csv', header=0)
print(f"Array Size (Rows, Columns): {df.shape}")

col_sum = df.sum(axis=0) #0 is for vertical move of the header
col_avg = df.mean(axis=0) #0 is for vertical move of the header

df.loc['SumOfTheColumn'] = col_sum
df.loc['AverageOfTheColumn'] = col_avg


df['SumOfTheRow'] = df.sum(axis=1) #1 is for vertical move of the header
df['AverageOfTheRow'] = df.mean(axis=1) #1 is for vertical move of the header
print(df.to_string())