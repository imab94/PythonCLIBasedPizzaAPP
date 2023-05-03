import pandas as pd

class DataPreprocessing:

    def __init__(self):
        self.temp = None
        self.row = None
        self.__data = pd.read_excel("Pizza.xlsx", sheet_name="Sheet1")

    def pizza_details(self,row):
        self.row = row
        self.temp = self.__data.iloc[self.row]
        return self.temp

    def pizza_menu(self):
        return self.__data


