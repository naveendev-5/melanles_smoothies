# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize your smoothie! :cup_with_straw: ")
st.write(
  """choose the fruits in your custom smoothie
  """)

name_on_order= st.text_input("Name on Smoothie:")
st.write("The name of your smoothie will be",name_on_order)
cnx=st.connection("snowflake")
session=cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingridients_list=st.multiselect(
     'choose upto 5 ingridients:'
     ,my_dataframe
     ,max_selections=5
 )
if ingridients_list:
    
   ingridients_string='';
   for fruit_chosen in ingridients_list:
       ingridients_string+= fruit_chosen + ' ';
      
   #st.write(ingridients_string)

   my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingridients_string + """','""" + name_on_order + """')"""

   st.write(my_insert_stmt)
 
   time_to_insert=st.button('submit order')
   if time_to_insert:
       #session.sql(my_insert_stmt).collect()
       
       st.success('Your Smoothie is ordered!', icon="✅")
