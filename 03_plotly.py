import streamlit as st
import pandas as pd
import plotly.express as px


# import datasets
st.title('Plotly or Streamlit ko mila k app bana')
df = px.data.gapminder()
st.write(df)
st.write(df.columns)
# summery
st.write(df.describe())

# Data Managment
year_option = df['year'].unique().tolist()

year = st.selectbox('Which year should we Plot?', year_option, 0)

#df = df[df['year']==year]


# using plotly
fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='continent',
                 log_x=True, size_max=55, range_x=[100, 100000], range_y=[20,90],
                 animation_frame='year', animation_group='continent')

st.write(fig)