import streamlit
import pandas as pd
import requests
import snowflake.connector
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
# New header from fruity vice
streamlit.header("Fruity Vice Fruit Advice!!")

fruit_choice = streamlit.text_input('What fruit would you like infomration about?', 'kiwi')
streamlit.write("The user entered", fruit_choice)

fruityvice_reponse = requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)
#use pandas to normalize the json format
fruityvice_normalized = pd.json_normalize(fruityvice_reponse.json())
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)


