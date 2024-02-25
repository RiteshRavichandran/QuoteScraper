# pip install beautifulsoup4
# pip install streamlit
# pip install requests
# Run this comand from the project file "streamlit run QuoteGen.py"

import streamlit as st
import pandas as pa 
import requests
from bs4 import BeautifulSoup

st.title("Quote Generator 🤩")
st.subheader("", divider="rainbow")
tag = str(st.selectbox('Choose a topic', ['Love', 'Humor', 'Life', 'Books', 'Friendship', 'Truth', 'Simile'])).lower()

url = f"https://quotes.toscrape.com/tag/{tag}/"

res = requests.get(url)

content = BeautifulSoup(res.content, 'html.parser')

quotes = content.find_all('div', class_='quote')

for quote in quotes:
    
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    link = quote.find('a')
    st.success(text)
    st.markdown(f"<a href=https://quotes.toscrape.com{link['href']}>{author}</a>", unsafe_allow_html=True)
    st.divider()

st.balloons()
st.caption('Made with ❤️ by Ritesh')
