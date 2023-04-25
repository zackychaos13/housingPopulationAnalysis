import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys # Use to close program when option 3 is selected

# class to pull specific data from Housing.csv
class HOUSING:
    def __init__(self, line):
        self.data = line
        self.age = self.data[0].strip()
        self.bedrms = self.data[1].strip()
        self.built = self.data[2].strip()

# read Housing.csv
housing = list()
with open('Housing.csv', 'r') as housing_data:
    reader = csv.reader(housing_data)
    next(reader)
    for line in reader:
        housing.append(HOUSING(line))

# class to pull specific data from PopChange.csv
class POP:
    def __init__(self, line):
        self.data = line
        self.apr = self.data[4].strip()
        self.jul = self.data[5].strip()
        self.change = self.data[6].strip()


# read PopChange.csv
pop = list()
with open('PopChange.csv', 'r') as pop_data:
    reader = csv.reader(pop_data)
    next(reader)
    for line in reader:
        pop.append(POP(line))


def histogram(col):  # copied from assignment to produce graph. not sure what values need to change
    # Fixing random state for reproducibility
    np.random.seed(214801)
    mu, sigma = 10, 5
    x = mu + sigma * np.random.randn(10000)
    #remove outliers
    col_rem = col[(col>col.quantile(0.01))&(col<col.quantile(0.99))]
    n, bins, patches = plt.hist(col_rem.values, bins=15,density=True, facecolor="b", alpha=0.75)
    plt.grid(True)
    # Assign to a figure
    fig1 = plt
    # Save Figure for Download
    fig1.savefig('display5.svg')
    plt.close('all')

# calculate different math functions for data
# calculations are not clean when printed
def calculations(col):
    histogram(col) # Run this outside of print statement - JD
    col = col.values
    print("\nThe statistics for this column are: ")
    # Use col.size. Pandas returns an array of numerical values from its read_csv function, which you are passing in. Since arrays have the 'size' attribute
    # that should work fine. I'm not sure if np.count() was or still is a numpy function, but shouldn't be necessary here! - JD
    print("Count =", col.size) # not the right function?
    print("Mean =", np.mean(col))
    print("Standard Deviation =", np.std(col))
    print("Min =", np.min(col))
    print("Max 1=", np.max(col))
    print("The Histogram of this column can be downloaded now.\n")  # histogram needs to be created
    print(col)

    show_menu()

# Put all of code for the menu in its own function. Since the user will be running calculations()
# no matter what, calculations() can restart the menu when it completes its tasks - JD
def show_menu():
    # welcome prompt
    print("Welcome to the Python Data Analysis App")
    print("\nSelect the file you want to analyze:\n")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")

    choice = int(input())
    # if statements to execute user choice

    if choice == 1:
        print("\nYou have selected Population Data.")
        print("Select the column you want to analyze:\n")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit Column")
        option = str(input())


        # options select specific data from csv.
        # calculations are not clean when printed
        if option == 'a':
            print("\nYou selected Pop Apr 1")
            col=pd.read_csv('PopChange.csv', usecols=['Pop Apr 1'])
            print(calculations(col))
            return col
        elif option == 'b':
            print("\nYou selected Pop Jul 1")
            col=pd.read_csv('PopChange.csv', usecols=['Pop Jul 1'])
            print(calculations(col))
        elif option == 'c':
            print("\nYou selected Change Pop")
            col=pd.read_csv('PopChange.csv', usecols=['Change Pop'])
            print(calculations(col))
        elif option == 'd':
            print("\nLeaving Population Data\n")  # need to leave pop data to main menu
            show_menu() # restart menu - JD
            # how to loop back to welcome?
        else:
            print("\nInvalid entry. Please try again.")

    # options select specific data from csv.
    # insert calculations() into each option
    elif choice == 2:
        print("You have selected Housing Data.")
        print("Select the column you want to analyze:\n")
        print("a. Age")
        print("b. Bedrooms")
        print("c. Year Built")
        print("d. Exit Column")
        option = str(input())

        # options select specific data from csv.
        # calculations are not clean when printed
        if option == 'a':
            print("You selected Age")
            col=pd.read_csv('Housing.csv', usecols=['AGE'])
            print(calculations(col))
        elif option == 'b':
            print("You selected Bedrooms")
            col=pd.read_csv('Housing.csv', usecols=['BEDRMS'])
            print(calculations(col))
        elif option == 'c':
            print("You selected Year Built")
            col=pd.read_csv('Housing.csv', usecols=['BUILT'])
            print(calculations(col))
        elif option == 'd':
            print("Leaving Housing Data\n")  # need to leave pop data to main menu
            # loop back to Welcome?
            show_menu() # restart menu - JD
        else:
            print("Invalid entry. Please try again.")

    elif choice == 3:
        print("Thank you for using the Python Data Analysis App")
        #sys.exit(0) # Closes the program when user chooses 3  - JD
    # break
    else:
        print("Invalid entry. Please try again.")

col=show_menu()