import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(datapath):
    border = "-"*40

    # Step 1 : Load the dataset from CSV file
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(datapath)
    print(border)
    print("Some Entries from dataset : ")
    print(df.head())
    print(border)

    # Step 2 : Clean the dataset by removing empty rows

    print(border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(border)

    df.dropna(inplace = True)
    print("Total records : ",df.shape[0])
    print("Total Columns : ",df.shape[1])
    print(border)

    # Step 3 : Separate independent and dependent variables

    print(border)
    print("Step 3 : Separate independent and dependent variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(border)
    print("Input Columns : ",X.columns.to_list())
    print("Output Column : Class")

    # Step 4 : Split the dataset for training and testing

    print(border)
    print("Step 4 : Split the dataset for training and testing")
    print(border)

    X_train, X_test, Y_train,  Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

    print(border)
    print("information of training and testing data ")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    # Step 5 : Feature Scalling

    print(border)
    print("Step 5 : Feature Scalling")
    print(border)

    scaler = StandardScaler()

    # Independent Variable Scalling

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature scalling is done")

    # Step 6 : Explore multiple values of K
    # hyperparameter tuning (K)

    print(border)
    print("Step 6 : Explore multiple values of K")
    print(border)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test, Y_pred)

        accuracy_scores.append(accuracy)

    print(border)
    print("Accuracy report of all k values from 1 to 20")

    for value in accuracy_scores:
        print(value)

    print(border)

    # Step 7 : Plot graph of k verses Accuracy

    print(border)
    print("Step 7 : Plot graph of k verses Accuracy")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values, accuracy_scores, marker = 'o')
    plt.title("K values Verses accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()


def main():

    border = "-"*40
    print(border)
    print("Wine Classifier using KNN")

    MarvellousClassifier("WinePredictor.csv")

if __name__ =="__main__":
    main()

