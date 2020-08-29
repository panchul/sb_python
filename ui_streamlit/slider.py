#
# run
#    $ streamlit run slider.py
#
# then open `localhost:8501`
#
# See more at github.com/streamlit/streamlit
#

import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

