import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# make containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Kashti ki app')
    st.text("in this project we will work on Kashti data")

with data_sets:
    st.header("Kashti doob gaye")
    st.text("We will work on Titanic Dataset")
# import datasets
df = sns.load_dataset("titanic")
df = df.dropna()
st.write(df.head(10))

st.subheader('Secregate into Male and female')

st.bar_chart(df['sex'].value_counts())
# identify through class
st.subheader("Secregate in different class")
st.bar_chart(df['class'].value_counts())

# identify through age
st.subheader("identify through age")
st.bar_chart(df['age'].sample(10))

with features:
    st.header("these are our features")
    st.text("Awain bhot sary feature add karty hain")
    st.markdown("1. **features 1:** This will tell us how many ")

with model_training:
    st.header("Kashti walon ka kia bana? Model_Training")
    st.text("in it we will change our parameters")
    # Making Coloums
    input, disply = st.columns(2)
    # first coloumns slection points
    max_depth = input.slider("How many People do you know", min_value=10, max_value=100, value=20, step= 5)

# n_estimators
n_estimators = input.selectbox("How many tree should be there in a RF", options=[50, 100, 200, 300, "No Limit"])

#adding list of features
input.write(df.columns)
# input feature from user
input_features = input.text_input("Which feature we used")

# make the Machine Learning Models
model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
# if condition on No limits
if n_estimators == "No Limit":
    model = RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
#define X and y
X = df[[input_features]]
y = df[["fare"]]
# fit the model
model.fit(X, y)
pred = model.predict(y)

# Disply the metrics
disply.subheader("Mean Sequre Error of the model is")
disply.write(mean_squared_error(y, pred))
disply.subheader("Mean Absolute Error of the model is")
disply.write(mean_absolute_error(y, pred))
disply.subheader("R Sequre score of the model is")
disply.write(r2_score(y, pred))