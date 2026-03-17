import pandas as pd
import numpy as np
import joblib as  jb

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# ------------------------------------------------------------------------------------------
#   Function Name   :   TrainTitanicModel
#   Description     :   It does split x, y,training data, tetsing data
#   Parameter       :   df
#   Return          :   None
#   Data            :   14/3/2026
#   Author          :   Sakshi Bhapkar
# ------------------------------------------------------------------------------------------

def TrainTitanicModel(df):

    # Split features and labels
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    print("\nFeatures : ")
    print(X.head())

    print("\nLabel : ")
    print(Y)

    print("Shape of X : ",X.shape)
    print("Shape of Y :",Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train Shape : ",X_train.shape)
    print("X_test Shape : ",X_test.shape)
    print("Y_train Shape : ",Y_train.shape)
    print("Y_test Shape : ",Y_test.shape)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train,Y_train)

    print("Model Trained Successfully")

    print("\nIntercept of model :")
    print(model.intercept_)

    print("\nCoefficient of model : ")

    for feature,coefficient in zip(X.columns, model.coef_[0]):
        print(feature,":",coefficient)

# ------------------------------------------------------------------------------------------
#   Function Name   :   DisplayInfo
#   Description     :   It displays the formatted title
#   Parameter       :   title(str)
#   Return          :   None
#   Data            :   14/3/2026
#   Author          :   Sakshi Bhapkar
# ------------------------------------------------------------------------------------------

def DisplayInfo(title):
    print("\n"+"="*70)
    print(title)
    print("="*70)

# ------------------------------------------------------------------------------------------
#   Function Name   :   ShowData
#   Description     :   It shows basic information about dataset
#   Parameter       :   DataSet (df)
#                       df -> Pandas dataframe object
#                       message
#                       message -> Heading text to display
#   Return          :   None
#   Data            :   14/3/2026
#   Author          :   Sakshi Bhapkar
# ------------------------------------------------------------------------------------------

def ShowData(df, message):
    DisplayInfo(message)

    print("First 5 rows of dataset : ")
    print(df.head())

    print("\n Shape of dataset")
    print(df.shape)

    print("\nColumn names : ")
    print(df.columns.tolist())

    print("\nMissing Values in each columns ")
    print(df.isnull().sum())

# ------------------------------------------------------------------------------------------
#   Function Name   :   MarvellousTitanicLogistic
#   Description     :   This is main pipeline controller
#                       It loads the dataset, show the raw data, 
#                       it preprocess the dataset and train the model
#   Parameter       :   Data path of dataset file
#   Return          :   None
#   Data            :   14/3/2026
#   Author          :   Sakshi Bhapkar
# ------------------------------------------------------------------------------------------

def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1: Loading the DataSet")

    df = pd.read_csv(DataPath)

    ShowData(df,"Initial Dataset")

    df = CleanTitanicData(df)

    TrainTitanicModel(df)

# ------------------------------------------------------------------------------------------
#   Function Name   :   CleanTitanicData
#   Description     :   It does preprocessing
#                       It removes unneccessary columns
#                       It handles missing values
#                       It converts text data to numeric format
#                       It does encoding to categorical columns
#   Parameter       :   df -> pandas dataframe
#   Return          :   df -> cleaned pandas dataframe 
#   Data            :   14/3/2026
#   Author          :   Sakshi Bhapkar
# ------------------------------------------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 : Original Data : ")

    print(df.head())

    # Remove unneccessary columns
    drop_columns = ["Passengerid","zero","Name","Cabin"]

    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\nColumns to be dropped : ")
    print(existing_columns)

    # drop the unwanted columns
    df = df.drop(columns = existing_columns)
    DisplayInfo("Step 2 : Data after columns removal : ")
    print(df.head())

    # Handle age column

    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))

        #  invalid value gets converted as NaN
        df["Age"] = pd.to_numeric(df["Age"], errors = "coerce")

        age_median = df["Age"].median()

        #  Replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\nAge column after preprocessing :")
        print(df["Age"].head(10))

    #  Handle fare column
    if "Fare" in df.columns:
        print("\n Fare column before preprocessing : ")
        print(df["Fare"].head(10))

        fare_median = df["Fare"].median()

        print("\n Median of Embarked column : ",fare_median)

        #  Replace missing values with median
        df["Fare"] = df["Fare"].fillna(fare_median)

    # handle Embarked column
    if "Embarked" in df.columns:
        print("\n Embarked column before preprocessing : ")
        print(df["Embarked"].head(10))

        # Convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # remove missing values
        df["Embarked"] = df["Embarked"].replace(['nan','none',''],np.nan)

        # Get most frequent value
        embark_mode = df["Embarked"].mode()[0]
        print("Mode of embarked column : ",embark_mode)

        df["Embarked"] = df["Embarked"].fillna(embark_mode)

        print("\nEmbarked column after preprocessing :")
        print(df["Embarked"].head(10))

    # Handle Sex column

    if "Sex" in df.columns:
        print("Sex column before filling missing values")
        print(df["Sex"].head(10))

        #  invalid value gets converted as NaN
        df["Sex"] = pd.to_numeric(df["Sex"], errors = "coerce")

        print("\nSex column after preprocessing :")
        print(df["Sex"].head(10))

    DisplayInfo("Data After preprocessing")
    print(df.head())

    print("Missing values after preprocessing")
    print(df.isnull().sum())

    # Encode Embarked column
    
    df = pd.get_dummies(df,columns=["Embarked"],drop_first=True)
    print("\nData after encoding")
    print(df.head())
    print("Shape of dataset : ",df.shape)

    #  convert boolean columns into integer

    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\nData after encoding")
    print(df.head())

    return df

# ------------------------------------------------------------------------------------------
#   Function Name   :   main
#   Description     :   Starting point of the application
#   Parameter       :   None
#   Return          :   None
#   Data            :   14/3/2026
#   Author          :   Sakshi Bhapkar
# ------------------------------------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")


if __name__ == "__main__":
    main()