import streamlit
import pandas as pd

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('First Snowflake Streamlit App')

streamlit.header('This is a streamlist header')

streamlit.text('Some streamlit Text')

streamlit.text('Some more streamlit text')

streamlit.text('Look! emojis! 🥣 🥗 🐔 🥑🍞')

streamlit.header('🍌🥭 Fruit Header! 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)



