'''import streamlit as st
import requests

# ===== Gemini API setup =====
GEMINI_API_KEY = "" 
GEMINI_MODEL = "gemini-2.0-flash" # or "gemini-2.0-flash"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# ===== Function to call Gemini API =====
def get_gemini_response(word):
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"parts": [{"text": f"Explain the word '{word}' in one short sentence."}]}
        ]
    }
    params = {"key": GEMINI_API_KEY}

    response = requests.post(GEMINI_API_URL, headers=headers, json=payload, params=params)

    if response.status_code == 200:
        data = response.json()
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"].strip()
        except:
            return "Could not extract explanation."
    else:
        return f"Error: {response.status_code} - {response.text}"

# ===== Streamlit UI =====
st.set_page_config(page_title="Notz", page_icon="📝")
st.title("📝 Notz - The Word Explainer Chat")
st.markdown("Ask Notz to explain any word in a short sentence!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
with st.form("word_form", clear_on_submit=True):
    user_input = st.text_input("Enter a word to get explanation:")
    submit = st.form_submit_button("Explain")

if submit and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    notz_reply = get_gemini_response(user_input)
    st.session_state.messages.append({"role": "notz", "content": notz_reply})

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div style='text-align:right; background-color:#1e1e1e; color:white; padding:10px; border-radius:10px; margin:5px 0'>{msg['content']}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div style='text-align:left; background-color:#d3d3d3; color:black; padding:10px; border-radius:10px; margin:5px 0'><strong>Notz:</strong> {msg['content']}</div>",
            unsafe_allow_html=True,
        )'''


import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# ===== Gemini API setup =====
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Set environment variable.")

GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# ===== Function to call Gemini API =====
def get_gemini_response(word):
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"parts": [{"text": f"Explain the word '{word}' in one short sentence."}]}
        ]
    }
    params = {"key": GEMINI_API_KEY}
    response = requests.post(GEMINI_API_URL, headers=headers, json=payload, params=params)
    
    if response.status_code == 200:
        data = response.json()
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"].strip()
        except:
            return "Could not extract explanation."
    else:
        return f"Error: {response.status_code} - {response.text}"

# ===== Streamlit UI =====
st.set_page_config(page_title="Notz", page_icon="📝")
st.title("📝 Notz - The Word Explainer")
st.markdown("Enter a word to get its meaning in one short sentence.")

# User input
word = st.text_input("Enter a word:")

if word:
    meaning = get_gemini_response(word)
    # Display the word and its meaning, left-aligned, full-width
    st.markdown(f"""
        <div style='text-align:left; background-color:#f0f0f0; color:#000; padding:15px; border-radius:10px; width:100%; margin-top:10px;'>
            <strong>Notz:</strong> {meaning}
        </div>
    """, unsafe_allow_html=True)




