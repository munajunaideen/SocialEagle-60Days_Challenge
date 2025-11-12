import streamlit as st
import random

# List of creative compliments
compliments = [
    "You're shining brighter than ever ✨",
    "Keep being amazing 🚀",
    "The world is better with you in it 🌍",
    "Age is just a number – you rock! 🤘",
    "Stay curious, stay awesome 💡",
    "You bring color to our lives 🌈",
    "Your smile can light up any room 😁"
]

def age_note(age):
    if age < 18:
        return "🌟 The future is yours!"
    elif age < 30:
        return "🔥 The best adventures are just beginning!"
    elif age < 60:
        return "💼 Success follows your steps."
    else:
        return "🌿 Age is wisdom, and wisdom is a treasure!"

st.markdown("""
    <style>
    .main-title {
        color: #ff6f61;
        font-size: 36px;
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-bottom: 30px;
    }
    .greeting-message {
        background: linear-gradient(90deg, #fdeff9, #ec38bc, #7303c0, #03001e);
        color: #fffbe7;
        padding: 18px;
        border-radius: 13px;
        font-size: 23px;
        margin-top: 30px;
        text-align: center;
        box-shadow: 0 2px 15px rgba(236, 56, 188, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🚀 Greeting Form</div>', unsafe_allow_html=True)

with st.form("creative_form"):
    name = st.text_input("Enter your name")
    age = st.slider("Select your age", 1, 100, 25)
    submitted = st.form_submit_button("Submit")

    if submitted:
        compliment = random.choice(compliments)
        personalized_note = age_note(age)
        html_greeting = (
            f'<div class="greeting-message">'
            f'👋 <b>Hello, <span style="color:#fde045;">{name}</span>!</b><br><br>'
            f'{compliment}<br>'
            f'You are <b style="color:#f94d6a;">{age}</b> years young.<br>'
            f'{personalized_note}'
            f'</div>'
        )
        st.markdown(html_greeting, unsafe_allow_html=True)
