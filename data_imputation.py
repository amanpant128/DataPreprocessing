import pandas as pd
from data_description import dataDescription

class Imputation:
    # task associated with this class
    tasks = [
        "\n1. Show number of Null Values",
        "2. Remove the Columns",
        "3. Fill the null values with mean",
        "4. Fill the null values with median",
        "5. Fill null values with mode",
        "6. Show the dataset"
    ]

    def __init__(self,data):
        self.data = data

    # this function will show the columns of the dataframe
    def showColumns(self):
        print("\nColumns\n")
        for column in self.data.columns.values:
            print(column, end = " ")
        return

    # this function will print the number of null values present in each column
    def printNullValues(self):
        print("\nNull values of each columns")
        for column in self.data.columns.values:
            # isnull checks the value of a column that whether the value is null or not
            print('{0: <20}'.format(column)+'{0: <5}'.format(sum(pd.isnull(self.data[column]))))
        print("")
        return

    # function which removes the null from the dataset
    def removeColumn(self):
        self.showColumns()
        while(1):
            columns = input("\nEnter all the column you want to delete(Press -1 to go back)")

            if columns == -1:
                break

            choice = input("Are you sure?(y/n) ")
            if choice == "y" or choice == "Y":
                try:
                    # inplace has to be true otherwise the changes will not reflect
                    self.data.drop(columns.split(" "), axis=1, inplace=True)
                except KeyError:
                    print("One or more columns are not present. Try again")
                    continue
                print("Done")
                break
            else:
                print("Not deleting")
            return

    # function to remove the nulls with mean
    def fillNullWithMean(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name. (Press -1 to go back) ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n) ")
            if choice == "y" or choice == "Y":
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mean())
                except KeyError:
                    print("Column is not present. Try again.")
                    continue
                except TypeError:
                    # Imputation is possible on some specific datatype like int, float etc.
                    print("The Imputaion is not possible here. Try on another column")
                    continue
                print("Done")
                break
            else:
                print("Not changing.")
        return

    #function to remove null with median
    def fillNullWithMedian(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name. (Press -1 to go back) ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n) ")
            if choice == "y" or choice == "Y":
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].median())
                except KeyError:
                    print("Column is not present. Try again.")
                    continue
                except TypeError:
                    # Imputation is possible on some specific datatype like int, float etc.
                    print("The Imputaion is not possible here. Try on another column")
                    continue
                print("Done")
                break
            else:
                print("Not changing.")
        return

    #function which removes the nulls with mode
    def fillNullWithMode(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name. (Press -1 to go back) ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n) ")
            if choice == "y" or choice == "Y":
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mode())
                except KeyError:
                    print("Column is not present. Try again.")
                    continue
                except TypeError:
                    # Imputation is possible on some specific datatype like int, float etc.
                    print("The Imputaion is not possible here. Try on another column")
                    continue
                print("Done")
                break
            else:
                print("Not changing.")
        return

    # Main function of the imputation class
    def imputer(self):
        while(1):
            print("\n Imputaion Tasks")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input(("\nWhat you want to do? (Prezz -1 to go back) ")))
                except ValueError:
                    print("Integer Value required. Try again")
                    continue
                break

            if choice == -1:
                break
            elif choice == 1:
                self.printNullValues()
            elif choice == 2:
                self.removeColumn()
            elif choice == 3:
                self.fillNullWithMean()
            elif choice == 4:
                self.fillNullWithMedian()
            elif choice == 5:
                self.fillNullWithMode()
            elif choice == 6:
                dataDescription.showDataset(self)
            else:
                print("\nWrong Integer Value. Try again.")
        return self.data