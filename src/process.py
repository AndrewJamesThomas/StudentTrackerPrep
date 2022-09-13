import pandas as pd
from datetime import datetime
import xlwings as xw
FILE_NAME = "Quick Query 20220913-121846.csv"


class CleanStudentTracker:
    def __init__(self, file_name):
        """
        Loads raw data as a pandas dataframe
        :param file_name: str, name of the raw data file to be processed
        :return: pd.DataFrame
        """
        path = "data/raw/" + file_name
        self.df = pd.read_csv(path)

    def add_additional_cols(self):
        """
        Add additional columns that are required by StudentTracker. These will be unchanged every time.
        """
        self.df["record_type"] = "D1"
        self.df["ssn"] = ""
        self.df["blank_col"] = ""
        self.df["school_code"] = "001371"
        self. df["branch_code"] = "00"

    def format_cols(self):
        """
        Changes all fields to the correct formats and data types.
        """
        self.df["Middle"] = self.df["Middle"].str[:1]
        self.df["Birthdate"] = pd.to_datetime(self.df["Birthdate"]).dt.strftime("%Y%m%d")
        self.df["Application Slate ID"] = pd.to_datetime(self.df["Application Slate ID"]).dt.strftime("%Y%m%d")


if __name__ == "__main__":


    # order column appropriately
    cols = ["record_type", "ssn", 'first_name', 'middle_name', 'last_name', 'suffix', 'birthdate',
            'start_search_date', "blank_col", "school_code", "branch_code", 'application_id']
    df = df[cols]

    # Save to excel
    current_date = datetime.now().strftime("%Y%m%d")
    path = "data/clean/studenttracker_data_" + current_date + ".xlsx"
    df.to_excel(path, index=False)

    wb = xw.Book(path)
    ws = wb.sheets["Sheet1"]
    ws.range("1:1").clear_contents()

    # Add header
    ws.range("A1:G1").value = ["H1", "'001371", "'00", "University of Denver",
                               current_date,
                               "DA", "I"]

    # Add footer
    total_rows = len(df) + 2
    footer_cell_1 = "A" + str(total_rows)
    footer_cell_2 = "B" + str(total_rows)

    ws.range(footer_cell_1).value = "T1"
    ws.range(footer_cell_2).value = total_rows
