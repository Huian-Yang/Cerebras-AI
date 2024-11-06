import os
from dotenv import load_dotenv
from cerebras.cloud.sdk import Cerebras
import streamlit as st

load_dotenv()

client = Cerebras(api_key=os.getenv("CEREBRAS_API_KEY"))

st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("SereniSpace")

#-----------Welcome--------------
st.subheader("Welcome!")
name = st.text_input("Enter your name:")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if st.button("Submit", key='button 1'):
    st.write(f"Hello {name}, Welcome to SereniSpace! This is a protected space where you can share your feelings and relax!")

#----------AI ChatBot--------------
st.subheader("Talk to an AI!")
query = st.text_input("Enter your question:")

if st.button("Submit", key='button 2') and query:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model="llama3.1-8b",
    )
    response = chat_completion.choices[0].message.content

    st.session_state.chat_history.append(f"You: {query}")
    st.session_state.chat_history.append(f"AI: {response}")

    # st.write(response)
    st.text_area("Response", value=response)

st.subheader("Chat History")
for msg in st.session_state.chat_history:
    st.write(msg)
