from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Missão Secreta", page_icon="🕵️", layout="centered")

# Esconde o menu, cabeçalho e rodapé do Streamlit e tira as margens
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "missao_secreta.html").read_text(encoding="utf-8")
components.html(html, height=1100, scrolling=True)
