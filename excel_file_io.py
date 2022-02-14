from typing import Tuple
import pandas as pd


class FileRead():
    """
        read in excel files
        grab individual sheets
    """
    def __init__(self, filename:str = None) -> None:
        """
            set flags and column names for calculations and conditionals
        """
        self.read_file_flag = False
        self.get_flag = False
        
        self._set_address(filename)

        self.excel_source = pd.DataFrame()
        self.source_sheet = pd.DataFrame()


    def read_excel_source(self):
        """
        read the excel data source completely
        Returns:
            pd.DataFrame: returns the excel file and a read status flag
        """
        self.read_file_flag = 0
        try:
            self.excel_source = pd.read_excel(self.filename, sheet_name=None)
            self.read_file_flag = True

        except FileNotFoundError:
            print("FilRead-read_excel_source: file was not found.")
            self.read_file_flag = False
            return (self.read_file_flag, self.excel_source)

        
        return (self.read_file_flag, self.excel_source)

    def get_source_sheet(self, sheet_name: str) -> Tuple[bool, pd.DataFrame]:
        """grab the metric register sheet
        Returns:
            pd.DataFrame: returns the excel file and a read status flag
        """
        self._is_file_read()
        self.get_flag = False

        try:
            self.source_sheet = self.excel_source[sheet_name]
            self.get_flag = True
        except KeyError:
            self.get_flag = False
            print("FileRead get_source_sheet: sheet not available")
            return (self.get_flag, self.source_sheet)
        
        return (self.get_flag, self.source_sheet)


    def _set_address(self, filename: str):
        if filename is None:
            self.filename = "C:\\Users\\ssartipzadeh\\BDO Canada LLP\\Pretium Resources Inc. - General\\03 - Projects\\Data Jumpstart\\10. WIP\\Pretium_KPI_Database_V01.xlsx"

        else:
            self.filename = filename

    def _is_file_read(self):
        if self.read_file_flag is not True:
            print("FileRead: the source file has not been read")
