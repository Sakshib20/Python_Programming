import pandas as pd
  
Border ="-"*95

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)
passed = (df["FinalResult"]==1).sum()
failed = (df["FinalResult"]==0).sum()

print(Border)
print("total number of student are : ")
print(len(df))
print(Border)

print(Border)
print("total number of passed student are : ")
print(passed)
print(Border)

print(Border)
print("total number of failed student are : ")
print(failed)
print(Border)