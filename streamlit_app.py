import streamlit as st
import pandas as pd


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

st.title('My Parents New Healthy Diner')

st.header('Maxims en Colins menu')
st.text('🥣 Omega3 &  Blueberry Oatmeal')

st.text('🥗 Kale, Spinanch & Rocket Smoothie')

st.text('🐔 Hard-boiled Free-Range Egg')

st.text('🥑🍞 Avocado Toasts')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)

st.divider()
my_button = st.button(label="Click me")

st.divider()
