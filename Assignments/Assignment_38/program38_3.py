import pandas as pd
  
Border ="-"*95

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)
avg_study = (df["StudyHours"]).mean()
avg_attend = (df["Attendance"]).mean()
max_score = (df["PreviousScore"]).max()
min_sleep = (df["SleepHours"]).min()

print("Average Study Hours :",avg_study)
print("Avearge Attendance :",avg_attend)
print("Maximum Previous Score :",max_score)
print("Minimum sleep hours :",min_sleep)