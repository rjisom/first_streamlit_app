import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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
try: 
  # Search for fruits dynamically
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
    # normalize data in pandas dataframe
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    # wdisplay dataframe
    streamlit.dataframe(fruityvice_normalized)
 
except URLError as e:
  streamlit.error()

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Search for fruits dynamically
fruit_to_add = streamlit.text_input('What fruit would you like to add?')

if (len(fruit_to_add) != 0):
  my_cur.execute("INSERT into fruit_load_list values "+f"('{fruit_to_add}')")
  streamlit.write('Thanks for adding ', fruit_to_add)
#.execute("... WHERE my_column = %(name)s", {"name": value})

#my_data_rows.append(fruit_to_add)



