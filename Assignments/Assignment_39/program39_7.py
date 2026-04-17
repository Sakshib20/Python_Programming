import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

df = pd.read_csv("student_performance_ml.csv")


x = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
y = df['FinalResult']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

model = DecisionTreeClassifier()

model.fit(x_train,y_train)

xtest=[[6,85,66,7,7]]

y_pred = model.predict(xtest)

if y_pred[0] == 1:
    print("The student is PASS.")
else:
    print("The student is FAIL.")
