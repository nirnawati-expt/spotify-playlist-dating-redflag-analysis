import time
from datetime import date

import streamlit as st

# Mengambil fungsi khusus dari dalam package CLI Anda
from vibecheck.main import main

st.title("Check your spotify playlist vibe ✨")

# 1. Ambil input dari user Streamlit
input_playlist_link = st.text_input("Insert playlilst Link:")

input_apikey = st.text_input("Insert your Google AI Studio API key (let it empty if don't have it):")


def write_to_streamlit(message):
    st.write(message)


if st.button("✨ Vibe Check ✨"):

    if input_playlist_link:

        with st.status("Checking your spotify playlist vibe 🪩", expanded=True) as status:
            try:

                data_file = main(input_playlist_link,
                                 input_apikey if input_apikey != "" else st.secrets["GOOGLE_CLOUD_API_KEY"],
                                 callback_print=write_to_streamlit)

                if data_file:
                    filename = "output-" + date.today().strftime("%y%m%d") + ".txt"
                    st.write("💾 Mixing the final results... almost done!")
                    time.sleep(1)
                    st.write("Finished the vibe check 🪄 download the generated file to see the result 👀")
                    st.download_button(
                        label="📥 Check the result",
                        data=data_file,
                        file_name=filename,
                        mime="text/txt"
                    )
                    status.update(label="Finished the vibe check", state="complete", expanded=True)
                else:
                    status.update(label="Finished the vibe check", state="complete", expanded=True)

            except Exception as e:
                status.update(label="Finished the vibe check", state="complete", expanded=True)
    else:

        st.warning("Fill the playlist link first")
