import pandas as pd
import numpy as np
import joblib as  jb

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix

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