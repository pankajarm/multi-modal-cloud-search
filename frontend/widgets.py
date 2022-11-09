import streamlit as st
from helpers import set_bg_hack_url


def set_background_widget(background_url):
    set_bg_hack_url(background_url)

def sidebar_widget():
    st.sidebar.title("Options")

    input_media = st.sidebar.radio(label="Search with...", options=["text", "image"])

    st.sidebar.markdown(
        """Image-to-Image and Text-to-Image Search using:
        [Jina](https://jina.ai)
        [Streamlit](https://streamlit.io)
        """
    )

    st.sidebar.markdown(
        "[Repo link](https://github.com/pankajarm/multi-modal-cloud-search)"
    )
    
    # st.sidebar.markdown(
    #     "[Credits](https://github.com/k-zehnder/jina-clip-streamlit)"
    # )
    return input_media

    