import pandas as pd
import numpy as np
from src.process import CleanStudentTracker


def test_load_data():
    data = CleanStudentTracker("test_data.csv")
    assert isinstance(data.df, pd.DataFrame), "Dataframe did not load"
    assert data.df.shape[0] > 0, "No data loaded"
    assert data.df.shape[1] == 7, "Incorrect number of columns"


def test_format_cols():
    data = CleanStudentTracker("test_data.csv")
    data.format_cols()
    df = data.df
    assert df["middle_name"].apply(lambda x: x is np.nan or len(str(x)) <= 1).all(), "Incorrect Middle Name Field"
    assert df["birthdate"].dtype=='int64', "Bithdate has incorrect datatype (should be int)"
    assert df["birthdate"].apply(lambda x: x is np.nan or len(str(x)) == 8).all(), "Birthdate in incorrect format."
    assert df["start_search_date"].dtype == 'int64', "Search date has incorrect datatype (should be int)"
    assert df["start_search_date"].apply(lambda x: x is np.nan or len(str(x)) == 8).all(), "Search date in incorrect format."


