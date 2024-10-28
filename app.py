import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Hello Streamlit")

#Display simple text
st.write("This is a simple text")

df=pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': ['a', 'b', 'c']
})

# Display DataFrame
st.write("Here is the DataFrame")
st.write(df)

# Create a line chart

chart_data=pd.DataFrame(
    np.random.randn(10, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

st.write(chart_data)