import streamlit
import pandas as pd
import snowflake.connector

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

#fruityvice api
streamlit.header("Fruityvice Fruit Advice!")
# Search for fruits dynamically
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())

# normalize data in pandas dataframe
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# wdisplay dataframe
streamlit.dataframe(fruityvice_normalized)
