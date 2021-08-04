import pandas as pd


class Download:
    def __init__(self, data):
        self.data = data

    # download the modified DataFrame as .csv file
    def download(self):
        toBeDownload = {}
        for column in self.data.columns.values:
            toBeDownload[column] = self.data[column]

        newFileName = input(
            "\nEnter the FILENAME you want as named? (Press -1 to go back):  ")
        if newFileName == "-1":
            return
        newFileName = newFileName + ".csv"
        # index=False as this will not add an extra column of index.
        pd.DataFrame(self.data).to_csv(newFileName, index=False)

        print("Hurray!! It is done.")

        if input("Do you want to exit now? (y/n) ").lower() == 'y':
            print("Exiting.")
            exit()
        else:
            return