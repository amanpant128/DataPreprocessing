import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from data_description import dataDescription

class Categorical:
    tasks = [
        '\n1. Show categorical columns',
        '2. Performing one hot encoding',
        '3. Show the dataset'
    ]

    def __init__(self,data):
        self.data = data

    # this  function will show all the categorical columns and number of unique values in them
    def categoricalColumn(self):
        print('\n{0: <20}'.format("Categorical Column")+'{0: <5}'.format("Unique Values"))
        # selecting the columns with object data type which could be further categorize
        for column in self.data.select_dtypes(include="object"):
            print('{0: <20}'.format(column)+'{0: <5}'.format(self.data[column].nunique()))

    # function to encode any particular column
    def encoding(self):
        categorical_columns = self.data.select_dtypes(include="object")
        while(1):
            column = input("\nWhich column would you like to hot encode? (Press -1 to go back) ").lower()
            if column == -1:
                break
            # the encoding function is only for categorical columns
            if column in categorical_columns:
                self.data = pd.get_dummies(data=self.data,columns=[column])
                print("Encoding is done.")

                choice = input("Are there more columns to be encoded? (y/n) ")
                if choice == "y" or choice == "Y":
                    continue
                else:
                    self.categoricalColumn()
                    break
            else:
                print("Wrong Column Name. Try again.")

    # the main function of the categorical class
    def categoricalMain(self):
        while(1):
            print("\nTasks")
            for task in self.tasks:
                print(task)
            while (1):
                try:
                    choice = int(input(("\n\What you want to do? (Press -1 to go back) ")))
                except ValueError:
                    print("Integer value required. Try again.")
                    continue
                break
            if choice == -1:
                break
            elif choice == 1:
                self.categoricalColumn()
            elif choice == 2:
                self.categoricalColumn()
                self.encoding()
            elif choice == 3:
                dataDescription.showDataset(self)
            else:
                print("\nWrong integer value. Try again.")
        # return the data after modifying
        return self.data
