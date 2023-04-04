import streamlit
import pandas as pd

streamlit.title('First Snowflake Streamlit App')

streamlit.header('This is a streamlist header')

streamlit.text('Some streamlit Text')

streamlit.text('Some more streamlit text')

streamlit.text('Look! emojis! 🥣 🥗 🐔 🥑🍞')

streamlit.header('🍌🥭 Fruit Header! 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

streamlit.dataframe(my_fruit_list)
