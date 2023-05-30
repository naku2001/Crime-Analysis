

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset from Excel
url='https://drive.google.com/file/d/1t_p8kliEMoVe_jtgp3gSLcFsvcxTPa7w/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url)


# Page title
st.title('Crime Data Analysis')

# Sidebar filter
display_option = st.sidebar.radio("Display Option", ('Crime Data', 'Total Crimes Per Each Category', 'Total Crimes Per Year'))

# Filtered display
if display_option == 'Crime Data':
    # Display the dataset as a table
    st.subheader('Crime Data')
    st.write(data)

elif display_option == 'Total Crimes Per Each Category':
    # Group the data by category and calculate the sum of each year
    grouped_data = data.groupby('Category').sum().drop(['Province', 'Major cities'], axis=1)

    # Line chart for crime trends by category over the years
    st.subheader('Crime Trends by Category')
    fig, ax = plt.subplots()
    lines = sns.lineplot(data=grouped_data.T, ax=ax)
    plt.xlabel('Year')
    plt.ylabel('Number of Crimes')
    plt.xticks(rotation=45)

    # Add legend with categories beside the line graph
    categories = grouped_data.index
    lines.legend(labels=categories, title='Categories', loc='center left', bbox_to_anchor=(1, 0.5))

    st.pyplot(fig)
elif display_option == 'Total Crimes Per Year':
    # Group the data by category and calculate the sum of each year
    grouped_data = data.groupby('Category').sum().drop(['Province', 'Major cities'], axis=1)

    # Bar chart for total crimes by year
    st.subheader('Total Crimes by Year')
    fig, ax = plt.subplots()
    grouped_data.sum().plot(kind='bar', ax=ax)
    plt.xlabel('Year')
    plt.ylabel('Number of Crimes')
    plt.xticks(rotation=45)
    st.pyplot(fig)




