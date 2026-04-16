import pandas as pd
import matplotlib.pyplot as plt
  
df = pd.read_csv("student_performance_ml.csv")

data = df["Attendance"]
plt.boxplot(data)
plt.title("Attendance plot")
plt.show()