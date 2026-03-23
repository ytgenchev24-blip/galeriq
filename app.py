import streamlit as st 

st.title("Gallery from favourite animals")

if "animals" not in st.session_state:
  st.session.state_animals = []

st.header("Add animal")
name = st.text_input("Name")
description = st.text_area("Add description")
image_url = st.text_input("URL of the photo")

if st.button("Add"):
  if name and description and image_url:
    st.session_state.animals.append({
      "ime": name,
      "opisanie": description,
      "kartinka": image_url
    })
    st.success(f"{name} is added!")
else:
  st.warning("populnete vsichki poleta!")

  if st.session_state.animals:
    st.header("Remove animal")

names = []
for a in st.session_state.animals:
  names.append(a["name"])

  remove_name = st.selectbox("Choose animalcfor remove", names)

  if st.button("Remove"):
    for a in st.session_state.animals:
        if a["name"] == remove_name:
           st.session_state.animals.remove(a)
           break

st.success(f"(remove_name) e premahnato!")

st.header("Gallery")
if st.session_state.animals:
  cols = st.colums(3)
  for idx, animal in enumerate(st.session_state.animals):
      with cols[idx % 3]:
        st.subheader(animal["name"])
        st.image(animal["photo"], use_column_with=True)
        st.write(animal["description"])

else:
   st.info("Gallery is empty. Add animals!")
    
  

    
    
    
