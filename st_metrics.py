import streamlit as st
import pandas as pd

st.header ('academic performance')
st.metric(label="Score", value="70 Points", delta="1.2 Points")

df = pd.DataFrame({
    'Rank': [1,2,3,4,5],
    'Performer': [1,2,3,4,5],
    'Points': [10,20,30,40,50]
    })
df.index.name = False
st.write ('Hall of Fame', df)
