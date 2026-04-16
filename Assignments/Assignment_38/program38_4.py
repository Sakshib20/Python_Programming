import pandas as pd
  
Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print(df["FinalResult"].value_counts(normalize=True)*100)
