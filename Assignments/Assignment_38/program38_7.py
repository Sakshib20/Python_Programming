import pandas as pd
import matplotlib.pyplot as plt
  
Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

df.columns = df.columns.str.strip()
pass_student = df[df["FinalResult"]==1]
fail_student = df[df["FinalResult"]==0]

plt.scatter(pass_student['StudyHours'],pass_student['PreviousScore'],color='orange',label='pass(1)',alpha=0.7)
plt.scatter(fail_student['StudyHours'], fail_student['PreviousScore'], color='blue', label='Fail (0)', alpha=0.7)

plt.xlabel('Study Hours')
plt.ylabel('Previous Score')
plt.title('Study Hours vs Previous Score')
plt.legend() 
plt.show()