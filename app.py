import streamlit as st
from chatbot_backend import chatbot_response

# Page setup
st.set_page_config(page_title="AI-Driven Public Health Chatbot", layout="centered")

# Title and intro
st.markdown("<h2 style='text-align:center;'>🤖 AI-Driven Public Health Chatbot</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Ask about your symptoms and get possible diseases, medicines, and doctor recommendations.</p>", unsafe_allow_html=True)
st.divider()

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.markdown(f"🧍‍♂️ **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")

# Input field
user_input = st.text_input("Enter your symptom or question:")

# Send message
if st.button("Send"):
    if user_input.strip():
        st.session_state.messages.append(("user", user_input))
        response = chatbot_response(user_input)
        st.session_state.messages.append(("bot", response))
        st.experimental_rerun()

# Reset button
if st.button("Reset Chat"):
    st.session_state.messages = []
    st.success("Chat reset. You can start again!")
