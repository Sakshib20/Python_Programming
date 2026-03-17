import pandas as pd
import numpy as np
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

    #----------------------------------------------------------------
    #       Step 6 : Split Dataset into Independent and Dependent Variables
    #----------------------------------------------------------------

    print(Border)
    print("Step 6 : Split Dataset into Independent and Dependent Variables")
    print(Border)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of Independent Variable : ",X.shape)
    print("Shape of Dependent Variable : ",Y.shape)

    #----------------------------------------------------------------
    #       Step 7 : Split Dataset for training and testing
    #----------------------------------------------------------------

    print(Border)
    print("Step 7 : Split Dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    #----------------------------------------------------------------
    #       Step 8 : Create and train the model
    #----------------------------------------------------------------

    print(Border)
    print("Step 8 : Create and train the model")
    print(Border)

    model = LinearRegression()
    model.fit(X_train,Y_train)

    #----------------------------------------------------------------
    #       Step 9 : Test the model
    #----------------------------------------------------------------

    print(Border)
    print("Step 9 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    #----------------------------------------------------------------
    #       Step 10 : Evaluate the model
    #----------------------------------------------------------------

    print(Border)
    print("Step 10 : Evaluate the model")
    print(Border)

    mse = mean_squared_error(Y_test, Y_pred)
    rmse = np.sqrt(mse)
    R2 = r2_score(Y_test, Y_pred)

    print("mean Squared Error : ",mse)
    print("root mean Squared Error : ",rmse)
    print("R Squared value : ",R2)

    #----------------------------------------------------------------
    #       Step 11 : Calculate model coefficient
    #----------------------------------------------------------------

    print(Border)
    print("Step 11 : Calculate model coefficient")
    print(Border)

    for column, value in zip(X.columns, model.coef_):
        print(f"{column}:{value}")


def main():

    MarvellousAdvertisement("Advertising.csv")


if __name__ == "__main__":
    main()