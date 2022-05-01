import streamlit as st
from helpers import search_by_text
from widgets import sidebar_widget, set_background_widget


# NOTE: Must have indexed documents in "./workspace" directory for our encoder directory AND also have encoder_searcher actively running in background with port expose

# ---------- Main area
# set_background_widget(
#     background_url="https://giphy.com/embed/26ufbhlsi494xEGZ2"
# )
st.title("Multi-Modality Cloud Search")

# ---------- Sidebar
input_media = sidebar_widget()

# ---------- Wait for user inputs
if input_media == "text":
    text_query = st.text_input(label="Search term")
    text_search_button = st.button("Search")
    if text_search_button:
        matches = search_by_text(text_query, verbose=True)
        st.success("success")

# if "matches" in locals():
#     matches_list = list(matches["@m"])
#     text_score_dict = {match.text:match.scores["cosine"].value for match in matches_list}
#     text_id_dict = {match.text:match.id for match in matches_list}
#     sorted_text_score_dict = dict(sorted(text_score_dict.items(), key=lambda item: item[1]))
#     for t, s in sorted_text_score_dict.items():
#         #print(match.text)
#         text_cell, metric = st.columns([5, 3])
#         #set the text
#         text_cell.text(t)
#         #set the score
#         metric.button(key=text_id_dict[t], label=f"score: {s:.5f}")
#         metric.write(" ")

if "matches" in locals():
    print("matches found", matches)
    print("matches found", matches.summary())
    for match in list(matches["@m"]):
        print(match.text)
        text_cell, metric = st.columns([5, 3])
        
        text_cell.text(match.text)
        score = match.scores["cosine"].value
        
        metric.button(key=match.id, label=f"score: {score:.5f}")
        metric.write(" ")