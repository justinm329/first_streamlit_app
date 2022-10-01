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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_reponse = requests.get('https://fruityvice.com/api/fruit/'+ this_fruit_choice)
  #use pandas to normalize the json format
  fruityvice_normalized = pd.json_normalize(fruityvice_reponse.json())
  return fruityvice_nomalized
#NEW section to display fruityvice api response
streamlit.header("Fruity Vice Fruit Advice!!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like infomration about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
#streamlit.write("The user entered", fruit_choice)
#streamlit.header("The fruit load list contains:")
#snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
# add a button to load the fruit
if stremlit.button("Get Fruit Load List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

##my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

#add_my_fruit = streamlit.text_input('What fruit would you like to add?')
#streamlit.write(f"Thanks for adding {add_my_fruit}!!")
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

