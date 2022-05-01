import streamlit as st
from helpers import search_by_text, resize_image, search_by_image
from widgets import sidebar_widget, set_background_widget


## ---------- Main area
# set_background_widget(
#     background_url="https://giphy.com/embed/26ufbhlsi494xEGZ2"
# )
st.title("Multi-Modality Cloud Search")

# ---------- Sidebar
input_media = sidebar_widget()

# ---------- Wait for user inputs
# ---------- Wait for user inputs
if input_media == "text":
    text_query = st.text_input(label="Search term")
    text_search_button = st.button("Search")
    if text_search_button:
        matches = search_by_text(text_query)
        st.success("success")

elif input_media == "image":
    image_query = st.file_uploader(label="Image file")
    image_search_button = st.button("Search")
    if image_search_button:
        matches = search_by_image(image_query)
        st.success("success")

if "matches" in locals():
    for match in matches:
        print(match.uri)
        pic_cell, metric = st.columns([5, 3])
        image = resize_image(match.uri, resize_factor=3)
        
        pic_cell.image(image, use_column_width="auto")
        score = match.scores["cosine"].value
        
        metric.button(key=match.id, label=f"score: {score:.5f}")
        metric.write(" ")