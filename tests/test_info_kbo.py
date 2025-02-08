from kbostadium.info_kbo import info_kbo
import pandas as pd
import pytest

def test_info3():
    df = info_kbo(keyword="KT 위즈")
    assert isinstance(df,pd.DataFrame)

def test_info4():
    # When
    df = info_kbo(keyword="KT 위즈")
    # assert
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]["구단"] == "KT 위즈"                                                  
