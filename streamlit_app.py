import streamlit as st

st.title("🎈 fosy-jago")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

number = st.number_input("Insert a number")
st.write("The current number is ", number)
