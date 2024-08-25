import streamlit as st

col1, col2= st.columns(2)

with col1:
    st.image("images/ati.webp")

with col2:
    st.title("Atiyeh Alikhani")
    content="""
        Hi,i am atiyeh !\n
        I am a student of programming course (Python)👩🏼‍💻
        """
    st.write(content)