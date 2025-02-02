from kbostadium.info_sta import info_sta
import pandas as pd
import pytest

def test_info():
    df = info_sta("KT")
    assert isinstance(df,pd.DataFrame)
   # assert
