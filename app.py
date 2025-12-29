import streamlit as st
import requests

# ===== Gemini API setup =====
GEMINI_API_KEY = "AIzaSyAB6M5DrJz7tHnJEvejIRhfH0Mro0hgWVE"
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
