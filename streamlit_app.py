import streamlit
import pandas
import requests
import snowflake.connector
import snowflake.connector
from urllib.error import URLError

streamlit.title(' My parents New Healthy Diner')


streamlit.header('Breakfast Favourities')

streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text(' 🥗Kale ,Spinach &Rocket Smoothie')

streamlit.text(' 🥚Hard Boiled Free Range Egg')

streamlit.text('🥝 Avacodo Tost')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)
#create repetable block code (as function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
    
#New Section to display Fruitjuice API response
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice: 
      streamlit.error("Please selet a fruit to get information.")
      #streamlit.write('The user entered ', fruit_choice)
    else:
     #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
     #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     #streamlit.dataframe(fruityvice_normalized)
     back_from_function=get_fruityvice_data(fruit_choice)
     streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()
  
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +"kiwi")


# Take the jason version of response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output in the screen as table 
#streamlit.dataframe(fruityvice_normalized)

#streamlit.stop()

#import snowflake.connector
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()

streamlit.header("The Fruit Load list contains:")
#Snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()

#Add Button load fruit
if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)

#streamlit.stop()
#Allow the end user to add fruit list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('" + "papaya" + "')")
         return "Thanks for Adding" + new_fruit
    
add_my_fruit= streamlit.text_input('What fruit would you like add?')
if streamlit.button('Add a Fruit to the List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function= insert_row_snowflake(add_my_fruit)   
   streamlit.text(back_from_function)

streamlit.text('Thanks for adding jackfruit')

