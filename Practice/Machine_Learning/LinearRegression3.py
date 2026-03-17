import numpy as np
import matplotlib.pyplot as plt

def MarvellousPredictor():
    #Load the data

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variable : X - ",X)
    print("Values of Dependent Variable : Y - ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_mean is : ",mean_x)        # 3.0
    print("Y_mean is : ",mean_y)        # 3.6

    n = len(X)      # 5

    # Y = mX + c
    # m = (summ (X-X_bar)*(Y-Y_bar) / (summ(X-X_bar) **2)

    Numerator = 0
    Denominator = 0

    for i in range(n):
        Numerator = Numerator + ((X[i]- mean_x) * (Y[i]- mean_y))
        Denominator = Denominator + ((X[i]-mean_x)**2)

    m = Numerator / Denominator

    print("Slope of line : ",m)         # 0.4

    c = mean_y - (m*mean_x)

    print("Y intercept is : ",c)        # 2.4

    x = np.linspace(1,6,n)
    y = c + (m * x)

    plt.plot(x,y,color ='g', label = "Regression Line")
    plt.scatter(X,Y, color = "r", label = "Scatter Plot")

    plt.xlabel("X : Independent Variables")
    plt.ylabel("Y : Dependent Variables")
    
    plt.legend()
    plt.show()

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()