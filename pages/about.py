import streamlit as st

# Page title
st.title('About Project')

# Project description
st.header('CRIME DATA ANALYSIS')
st.write('This project aims to analyze crime data,predict and provide insights into crime trends and statistics.')

# Contributors
st.header('Contributors')
contributors = [
    {'name': 'Rutendo Chenga', 'id': 'R215971T'},
    {'name': 'Mapfumo Lucia Chido', 'id': 'R2113118T'},
    {'name': 'Wellington Chirimanzu', 'id': 'R217922J'},
    {'name': 'Wallinw Muradzikwa', 'id': 'R217037F'},
    {'name': 'Mduduzi Bukhosibethu', 'id': 'R2110106H'}
]

for contributor in contributors:
    st.write(f"- {contributor['name']} ({contributor['id']})")

