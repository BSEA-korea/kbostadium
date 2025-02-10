import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

#st.set_page_config(page_title="Main", page_icon="💜")
#st.markdown("# Main page 🐽")
#st.sidebar.markdown("# Main page 🐽")

st.title("KBO STADIUM")
st.write("""
information of  *kbo stadium*

![img](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20160928_209%2Fdreiwunsche_1475053425909KC3LP_PNG%2Fdfafdaf.PNG&type=sc960_832)""")


st.subheader("입력")
name = st.text_input("메뉴 이름", placeholder="예: 김치찌개")
# selectbox 사용
# member_name = st.text_input("먹은 사람", value="jiwon")
kbo_name = st.selectbox("먹은 사람", options =  list(members.keys()), index = list(members.keys()).index('jiwon'))
# member_id = members 의 키
member_id = members[kbo_name]

dt = st.date_input("먹은 날짜")

isPress = st.button("검색")

if isPress:
    if menu_name and member_id and dt:
        if insert_menu(menu_name, member_id, dt):
            st.success(f"검색 성공")
        else:
            st.error(f"검색 실패")
    else:
        st.warning(f"모든 값을 입력해주세요!")
