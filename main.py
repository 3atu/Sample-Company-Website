import streamlit as st
import pandas

df = pandas.read_csv("data.csv", sep=",")

#layout
st.set_page_config()
title1 = "The Best Company"
section1 = "Our Team"
content1 = "Company description"

st.title(title1)
st.text(content1)
st.header(section1)



col1, col2, col3 = st.columns(3)


with col1:
    for index, row in df[:4].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        #data_first_name = row['first name']
        #data_last_name = row['last name']
        #data_full_name = data_first_name + " " + data_last_name
        #data_full_name = data_full_name.title()

        data_role = row['role']
        data_image = "images/" + row['image']

        #st.header(data_full_name)
        st.text(data_role)
        st.image(data_image)

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        #data_first_name = row['first name']
        #data_last_name = row['last name']
        #data_full_name = data_first_name + " " + data_last_name
        #data_full_name = data_full_name.title()

        data_role = row['role']
        data_image = "images/" + row['image']

        #st.header(data_full_name)
        st.text(data_role)
        st.image(data_image)

with col3:
    for index, row in df[8:].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        #data_first_name = row['first name']
        #data_last_name = row['last name']
        #data_full_name = data_first_name + " " + data_last_name
        #data_full_name = data_full_name.title()

        data_role = row['role']
        data_image = "images/" + row['image']

        #st.header(data_full_name)
        st.text(data_role)
        st.image(data_image)




