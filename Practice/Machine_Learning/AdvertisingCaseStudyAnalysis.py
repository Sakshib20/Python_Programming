import pandas as pd
import numpy as py
import matplotlib.pyplot

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousAdvertisement(datapath):

    Border ="-"*40
    #----------------------------------------------------------------
    #       Step 1 : Load Dataset
    #----------------------------------------------------------------

    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)

    df = pd.read_csv(datapath)

    print("few records from the head")
    print(df.head())

    #----------------------------------------------------------------
    #       Step 2 : Remove Unwanted columns
    #----------------------------------------------------------------

    print(Border)
    print("Step 2 : Remove Unwanted columns")
    print(Border)

    print("Shape of dataset before removal",df.shape)
    
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape of dataset after removal",df.shape)

    print(Border)
    print("clean dataset is : ")
    print(Border)

    print(df.head())

    #----------------------------------------------------------------
    #       Step 3 : Check missing values
    #----------------------------------------------------------------

    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Missing values :",df.isnull().sum())

    #----------------------------------------------------------------
    #       Step 4 : Display Statistical Summary
    #----------------------------------------------------------------

    print(Border)
    print("Step 4 : Display Statistical Summary")
    print(Border)

    print(df.describe())

    #----------------------------------------------------------------
    #       Step 5 : Correlations between columns
    #----------------------------------------------------------------

    print(Border)
    print("Step 5 : Correlations between columns")
    print(Border)

    print("Correlation Matrix")
    print(df.corr())

def main():

    MarvellousAdvertisement("Advertising.csv")
    
    



if __name__ == "__main__":
    main()