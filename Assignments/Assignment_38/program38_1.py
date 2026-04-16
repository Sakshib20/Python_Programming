import pandas as pd
  
Border ="-"*95

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print(Border)
print("First 5 entries are : ")
print(df.head())
print(Border)

print(Border)
print("Last 5 entries are : ")
print(df.tail())
print(Border)

print(Border)
print("Total number of rows and columns : ")
print(df.shape)
print(Border)

print(Border)
print("List of column names : ")
print(list(df.columns))
print(Border)

print(Border)
print("Data type of each column : ")
print(df.dtypes)
print(Border)