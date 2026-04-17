import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

df = pd.read_csv("student_performance_ml.csv")

x = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
y = df['FinalResult']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

model1 = DecisionTreeClassifier(max_depth=1)

model1.fit(x_train,y_train)

model2 = DecisionTreeClassifier(max_depth=3)
model2.fit(x_train,y_train)

model3 = DecisionTreeClassifier()
model3.fit(x_train,y_train)

y_pred1 = model1.predict(x_test)
model1_acc = accuracy_score(y_test,y_pred1)

print(f"Model1 Accuracy is : {model1_acc* 100:.2f}")

y_pred2 = model2.predict(x_test)
model2_acc = accuracy_score(y_test,y_pred1)
print(f"Model2 Accuracy is : {model2_acc* 100:.2f}")

y_pred3 = model3.predict(x_test)
model3_acc = accuracy_score(y_test,y_pred1)
print(f"Model3 Accuracy is : {model3_acc* 100:.2f}")