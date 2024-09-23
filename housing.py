import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data (1990) by Linxi Xia')


df = pd.read_csv('housing.csv')


price_filter = st.slider('Minimal Median House Price:', 0, 500001, 200000)  # min, max, default


location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),  # options
    df.ocean_proximity.unique()   # defaults
)


income_level = st.sidebar.radio(
    "Select income level:",
    ('Low', 'Medium', 'High')
)


if income_level == 'Low':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] >= 4.5]


filtered_df = filtered_df[filtered_df['median_house_value'] >= price_filter]


filtered_df = filtered_df[filtered_df['ocean_proximity'].isin(location_filter)]


st.map(filtered_df)


st.subheader('Histogram of Median House Value')
plt.figure(figsize=(10, 6))
sns.histplot(filtered_df['median_house_value'], bins=30, kde=False)
plt.title('Distribution of Median House Value')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
st.pyplot(plt)










