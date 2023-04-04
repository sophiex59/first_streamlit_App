import streamlit
import pandas
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon" + fruit_choice)



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My Parents Healthy DIner")

streamlit.header('BreakYourFast Menu')
streamlit.text('Omega 🥣 3')
streamlit.text('Kal🥗e')
streamlit.text('Hard-Boiled🐔')
streamlit.text('Avo🥑🍞 Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What Fruil would you like info on?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

# normalises the json response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# outputs it as table
streamlit.dataframe(fruityvice_normalized)
