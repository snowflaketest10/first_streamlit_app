import streamlit
streamlit.title(' My parents New Healthy Diner')


streamlit.header('Breakfast Favourities')

streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text(' 🥗Kale ,Spinach &Rocket Smoothie')

streamlit.text(' 🥚Hard Boiled Free Range Egg')

streamlit.text('🥝 Avacodo Tost')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
