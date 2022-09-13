import pandas as pd
import numpy as np
import os
from src.process import CleanStudentTracker

data = CleanStudentTracker("test_data.csv")


def test_load_data():
    assert isinstance(data.df, pd.DataFrame), "Dataframe did not load"
    assert data.df.shape[0] > 0, "No data loaded"
    assert data.df.shape[1] == 7, "Incorrect number of columns"


def test_add_additional_cols():
    data.add_additional_cols()
    new_cols = ["record_type", "ssn", "blank_col", "school_code", "branch_code"]

    assert all([x in data.df.keys() for x in new_cols]), "check column names. Are there enough?"
    assert all(data.df["record_type"] == "D1"), "Error in record type."
    assert all(data.df["ssn"] == ""), "Error in SSN"
    assert all(data.df["blank_col"] == ""), "Error in Blank Col"
    assert all(data.df["school_code"] == "001371"), "Error in school code"
    assert all(data.df["branch_code"] == "00"), "Error in branch code"


def test_format_cols():
    data.format_cols()
    df = data.df
    assert df["Middle"].apply(lambda x: x is np.nan or len(str(x)) <= 1).all(), "Incorrect Middle Name Field"
    assert df["Birthdate"].apply(lambda x: x is np.nan or len(str(x)) == 8).all(), "Birthdate in incorrect format."
    assert df["Application Slate ID"].apply(lambda x: x is np.nan or len(str(x)) == 8).all(), "Search date in incorrect format."


def test_rearrange_cols():
    data.rearrange_cols()
    df = data.df
    correct_cols = all(["record_type", "ssn", 'First', 'Middle', 'Last', 'Suffix', 'Birthdate', 'Submitted',
                        "blank_col", "school_code", "branch_code", 'Application Slate ID'] == df.keys())
    assert correct_cols, "Check column names and order"


def test_save_to_excel():
    data.save_to_excel("test_output")
    saved_files = os.listdir("data/clean")

    assert "test_output.xlsx" in saved_files, "File did not save appropriately."
