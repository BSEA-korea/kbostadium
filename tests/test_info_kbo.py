from kbostadium.info_sta import info_sta
import pandas as pd
import pytest

def test_info3():
    row_count = 3
    df = info_kbo(keyword="KT 위즈", rcnt=row_count)
    assert isinstance(df,pd.DataFrame)
   # assert

def test_info4():
    row_count = 7
    # When
    df = info_kbo(keyword="KT 위즈", rcnt=row_count)
    # assert
    assert isinstance(df, pd.DataFrame)
    assert len(df) < row_count
    #assert df.iloc[0]["구단"] == "키움 히어로즈"
~                                                   
