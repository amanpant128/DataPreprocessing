import pandas as pd


class dataDescription:
    tasks = ['\n1. Describe specific column',
             '2.Show properties per column',
             '3.Show Dataset']

    def __init__(self, data):
        self.data = data

    # function which will show dataset in screen
    def showDataset(self):
        while(1):
            try:
                rows = int(input(("\nEnter number of rows(>0) to print (Press -1 to go back)")))
                if rows == -1:
                    break
                if rows <=0:
                    print("Given rows must be +ve...")
                    continue
                print(self.data.head(rows))
            except ValueError:
                print("Numeric value is required. Enter again.....")
                continue
            break
        return
    # function which will print all the columns
    def showColumns(self):
        for column in self.data.columns.values:
            print(column, end=" ")

    # function which will describe the dataset or any specific column
    def describe(self):
        while(1):
            print("\nTasks(Data Description)\n")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back")))
                except ValueError:
                    print("Integer value required. Try again.")
                    continue
                break

            # conditions for choices
            if choice == -1:
                break
            elif choice == 1:
                self.showColumns()
                while(1):
                    describeColumn = input("\n\which Column? ").lower()
                    try:
                        # describe function will tell all the info regarding any specific column
                        print(self.data[describeColumn].describe())
                    except KeyError:
                        print("No column present with this name. Try again.")
                        continue
                    break
            elif choice == 2:
                # tells all the info about the dataset
                print(self.data.describe())
                print("\n\n")
                print(self.data.info())

            elif choice == 3:
                self.showDataset()

            else:
                print("\nWrong Integer Value. Try again.")