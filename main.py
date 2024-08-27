import streamlit as st
import pandas

col1, col2= st.columns(2)

with col1:
    st.image("images/ati.webp")

with col2:
    st.title("Atiyeh Alikhani")
    content="""
        Hi,i am atiyeh !\n
        I am a student of programming course (Python)👩🏼‍💻
        """
    st.info(content)

content2="""aaa👇"""

st.write(content2)

col3, col4= st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")

