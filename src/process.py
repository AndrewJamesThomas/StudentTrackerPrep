import pandas as pd
from datetime import datetime
import xlwings as xw

################################################
# UPDATE THIS
FILE_NAME = "Quick Query 20220913-121846.csv"
################################################


class CleanStudentTracker:
    def __init__(self, file_name):
        """
        Loads raw data as a pandas dataframe
        :param file_name: str, name of the raw data file to be processed
        :return: pd.DataFrame
        """
        path = "data/raw/" + file_name
        self.df = pd.read_csv(path)

        # check to make sure columns are appropriately named
        expected_col_names = ["Application Slate ID", "First", "Middle", "Last", "Suffix", "Birthdate", "Submitted"]
        assert all(expected_col_names == self.df.keys()), 'Error! Rename Columns to: "Application Slate ID", ' \
                                                                  '"First", "Middle", "Last", "Suffix", "Birthdate", ' \
                                                                  '"Submitted"'

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

    def rearrange_cols(self):
        """
        Reorder columns to be saved to Excel
        """
        cols = ["record_type", "ssn", 'First', 'Middle', 'Last', 'Suffix', 'Birthdate', 'Submitted', "blank_col",
                "school_code", "branch_code", 'Application Slate ID']
        self.df = self.df[cols]

    def save_to_excel(self, filename):
        """
        Saves the file as an excel workbook and adds the appropriate header/footer
        :param filename: str, name of the excel workbook that will be created.
        """
        # Save to excel
        path = "data/clean/" + filename + ".xlsx"
        self.df.to_excel(path, index=False)

        wb = xw.Book(path)
        ws = wb.sheets["Sheet1"]
        ws.range("1:1").clear_contents()

        # Add header
        ws.range("A1:G1").value = ["H1", "'001371", "'00", "University of Denver",
                                   datetime.now().strftime("%Y%m%d"),
                                   "DA", "I"]

        # Add footer
        total_rows = len(self.df) + 2
        footer_cell_1 = "A" + str(total_rows)
        footer_cell_2 = "B" + str(total_rows)

        ws.range(footer_cell_1).value = "T1"
        ws.range(footer_cell_2).value = total_rows

    def process_all_data(self, output_filename):
        self.add_additional_cols()
        self.format_cols()
        self.rearrange_cols()
        self.save_to_excel(output_filename)


if __name__ == "__main__":
    data = CleanStudentTracker(FILE_NAME)
    data.process_all_data()
