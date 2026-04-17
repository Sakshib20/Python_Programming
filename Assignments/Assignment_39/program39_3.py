import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")

x = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
y = df['FinalResult']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

model = DecisionTreeClassifier()

model.fit(x_train,y_train)
print("Training done")

Y_pred = model.predict(x_test)


print("Accuracy Score is : ",accuracy_score(y_test,Y_pred)*100,"%")
