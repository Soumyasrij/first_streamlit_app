import streamlit

streamlit.title('My Parents new Healthy Diner')

streamlit.header('Breakfast Favourites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
               
streamlit.text('🥗 kale, spinach & rocket smoothie')

streamlit.text('🐔 Hard Boiled free range egg')

streamlit.text('🥑🍞 Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +  fruit_choice)


# normalize response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output
streamlit.dataframe(fruityvice_normalized)
