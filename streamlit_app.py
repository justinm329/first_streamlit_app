import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Parents New Healthy Diner")


streamlit.header("Breakfast Menue")
streamlit.text("🥣 Oatmeal with fresh fruit and maple syrup")
streamlit.text("🥗 Kale and Spinach Rocket Smoothie")
streamlit.text("🐔 Free Range Eggs with wheat toast and Fresh Fruit")
streamlit.text("🥑🍞 Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_list = fruit_list.set_index("Fruit")
fruits_selected = streamlit.multiselect("Pick Some Fruits:", list(fruit_list.index)) #,["Avocado", "Strawberries"])
fruits_to_show = fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
# create function for repeatable code

streamlit.header("Fruityvice Fruit advice")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruity_normalized)
except URLError as e:
  streamlit.error()

##my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

#add_my_fruit = streamlit.text_input('What fruit would you like to add?')
#streamlit.write(f"Thanks for adding {add_my_fruit}!!")
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

