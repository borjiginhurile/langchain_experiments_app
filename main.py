import langchain_helper as lch

import streamlit as st

st.title("Name your pet App")
animal_type = st.sidebar.selectbox("What is your pet animal type?", ["dog", "cat", "bird"])
pet_color = ""
if animal_type == "dog":
    pet_color = st.sidebar.text_area("What is your pet color?", max_chars=15)
elif animal_type == "cat":
    pet_color = st.sidebar.text_area("What is your pet color?", max_chars=15)
elif animal_type == "bird":
    pet_color = st.sidebar.text_area("What is your pet color?", max_chars=15)


if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    st.text(response)