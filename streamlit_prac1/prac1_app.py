import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# 헤드라인
st.write('여기에 lgbm_df 업로드 되어 있기 때문에 여기서 lgbm 실습')
st.write('---')

#### 데이터 불러오기 ####
st.write('#### 전처리한 데이터')
st.write('아 왜 자꾸 파일을 찾을 수 없대!!!!! git - lfs 문제인듯 빨리 해결해..')
# pkl_path = f"{os.path.dirname(os.path.abspath(__file__))}/lgbm_df.pkl"
# # lgbm_df = joblib.load('streamlit_prac1\lgbm_df.pkl')
# lgbm_df = joblib.load(pkl_path)
# lgbm_df = pd.DataFrame(lgbm_df)
# st.write(lgbm_df.head())
