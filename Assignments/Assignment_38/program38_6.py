import pandas as pd
import matplotlib.pyplot as plt
  
Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

plt.hist(df['StudyHours'], bins=10, color='skyblue', edgecolor='black')

plt.title('Histogram of Study Hours')
plt.xlabel('Hours Studied')
plt.ylabel('Number of Students')

plt.show()