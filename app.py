import streamlit as st
import requests

st.set_page_config(page_title="Notz", page_icon="📝")
st.title("📝 Notz - The Word Explainer")
st.write("Enter a word to get its meaning in one short sentence.  \nExample: Apple , Wind , Prime Number.. etc.")

def explain_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Word not found."

    data = response.json()
    try:
        return data[0]["meanings"][0]["definitions"][0]["definition"]
    except:
        return "Meaning not available."

word = st.text_input("Enter a word")

if word:
    meaning = explain_word(word)
    st.markdown(
        f"""
        <div style="background:#f0f0f0;color:#000;padding:15px;border-radius:10px">
            <strong>Notz:</strong> {meaning}
        </div>
        """,
        unsafe_allow_html=True
    )
