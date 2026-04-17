import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix


border = "-"*90

# --------------------------------------------------------------
# Step 1 : Load the dataset
# --------------------------------------------------------------

print(border)
print("Step 1 : Loading the  Dataset")
df = pd.read_csv("student_performance_ml.csv")
print("Data loaded successfully")
print(border)

# --------------------------------------------------------------
# Step 2 : Data Analysis
# --------------------------------------------------------------

print(border)
print("Step 2 : Data Analysis")
print("Shape of dataset",df.shape)
print("Missing Values per column : ")
print(df.isnull().sum())

print("Statistical report of dataset : ")
print(df.describe())

# --------------------------------------------------------------
# Step 3 : Visualization
# --------------------------------------------------------------

print(border)
print("Step 3 : Visualization")

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
print(border)

# --------------------------------------------------------------
# Step 4 : Split dataset for training and testing
# --------------------------------------------------------------

print(border)
print("Step 4 : Train - Test split")

x =df.drop("FinalResult",axis=1)
y = df["FinalResult"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print(border)

# --------------------------------------------------------------
# Step 5 : Training the model
# --------------------------------------------------------------

print(border)
print("Step 5 : Model Training")

model = DecisionTreeClassifier()

model.fit(x_train,y_train)

# --------------------------------------------------------------
# Step 6 : Test the model
# --------------------------------------------------------------
print(border)
print("Step 6 : Testing")

y_pred = model.predict(x_test)
print(border)

# --------------------------------------------------------------
# Step 7 : Accuracy Calculation
# --------------------------------------------------------------
print(border)
print("Step 7 : Accuracy Calculation")

accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy of model : {accuracy*100:.2f}")

# --------------------------------------------------------------
# Step 8 : Confusion Matrix generation
# --------------------------------------------------------------
print(border)
print("Step 8 : Confusion Matrix generation")
print(confusion_matrix(y_test,y_pred))

# --------------------------------------------------------------
# Step 9 : Final Conclusion
# --------------------------------------------------------------
print(border)
print("Step 9 : Final Conclusion")

if accuracy>0.8:
    print("Model is highly accurate")

else:
    print("Model is not that accurate")