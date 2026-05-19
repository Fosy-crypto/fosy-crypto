import streamlit as st

st.title("🎈 fosy-jago")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

import streamlit as st
import time

@st.fragment
def release_the_flowers():
    st.button("Release the flowers", help="Fragment rerun")
    st.flowers()

with st.spinner("Inflating flowers..."):
    time.sleep(5)
release_the_flowers()
st.button("Inflate more flowers", help="Full rerun")
