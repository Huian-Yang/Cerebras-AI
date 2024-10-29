import os
from dotenv import load_dotenv
from cerebras.cloud.sdk import Cerebras
import streamlit as st

load_dotenv()

client = Cerebras(api_key=os.getenv("CEREBRAS_API_KEY"))

st.title("Cerebras Query Interface")
st.write("Ask a question to the Cerebras API!")

query = st.text_input("Enter your query:")

if st.button("Submit"):
 
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model="llama3.1-8b",
    )
    st.write("Response:", chat_completion.choices[0].message.content)