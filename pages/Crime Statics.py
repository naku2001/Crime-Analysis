import streamlit as st
import pandas as pd

url='https://drive.google.com/file/d/1t_p8kliEMoVe_jtgp3gSLcFsvcxTPa7w/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url)

# Page title
st.title('Crime Data Statistics')

# Display the dataset as a table
st.subheader('Data Table')
st.write(data)

# Calculate statistics
statistics = {
    'Total Crimes': data.iloc[:, 3:].sum().sum(),
   
    'Total Provinces': data['Province'].nunique(),
    'Total Categories': data['Category'].nunique()
}

# Display the statistics
st.subheader('Statistics')
for stat_name, stat_value in statistics.items():
    st.write(f'- {stat_name}: {stat_value}')

# Bar chart for total crimes by year
st.subheader('Total Crimes by Year')
year_columns = [col for col in data.columns if col.startswith('20')]
yearly_total = data[year_columns].sum()
st.bar_chart(yearly_total)

# Bar chart for total crimes by province
st.subheader('Total Crimes by Province')
province_total = data.groupby('Province')[year_columns].sum()
st.bar_chart(province_total)

# Bar chart for total crimes by category
st.subheader('Total Crimes by Category')
category_total = data.groupby('Category')[year_columns].sum()
st.bar_chart(category_total)



