from os import P_PID
import streamlit as st
import pandas as pd 
import helper


st.write("# My First Rapid Dev App")

if st.button("Press me!"):
    pData, pIndex, pCols = helper.testFunktion()
    TestDF = pd.DataFrame(pData, pIndex, pCols)
    st.write(TestDF)