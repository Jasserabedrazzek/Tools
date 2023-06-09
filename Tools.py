import streamlit as st
from translate import Translator
from pytube import YouTube

st.set_page_config(
    page_title="Tools For You",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://jasserabedrazzek-message-compts-ce1kav.streamlit.app/",
        'About': "# Tools For U, enjoy it and if you encounter any problems, we are here to help."
    }
)

st.header("Welcome!")
cl1, cl2, cl3 = st.columns(3)
languages = ["English", "French", "ar", "Spanish", "German", "Italian", "Portuguese", "Japanese", "Chinese"]
with cl3:
    target_lang = st.selectbox("Select Language", languages)
translator = Translator(to_lang=target_lang)
mot = "Choose your option."
dow = "Download the video."
sp = "Convert text to speech."
cs = "Convert speech to text."
tst = "Test the Wi-Fi connection."
translation = translator.translate(mot)
if target_lang.lower() != "english":
    translation = translator.translate(mot)
tr_d = translator.translate(dow)
tr_sp = translator.translate(sp)
tr_cs = translator.translate(cs)
tr_tst = translator.translate(tst)
st.write(translation)
tab1, tab2, tab3, tab4 = st.tabs([tr_d, tr_sp, tr_cs, tr_tst])
with tab1:
    link = st.text_input("Enter the YouTube video URL: ")
    if link:
        youtubeObject = YouTube(link)
        stream = youtubeObject.streams.get_highest_resolution()
        video_title = youtubeObject.title
        st.download_button("Download", data=stream.download(), file_name=video_title, mime="video/mp4")
    else:
        st.warning("Please provide a YouTube video URL.")

