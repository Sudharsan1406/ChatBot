import streamlit as st
from groq import Groq
import json
import os

# -----------------------------
# GROQ API
# -----------------------------
client = Groq(
    api_key="Secret Key"
)

# -----------------------------
# MEMORY FILE
# -----------------------------
CHAT_FILE = "chat_history.json"

# Create file if not exists
if not os.path.exists(CHAT_FILE):
    with open(CHAT_FILE, "w") as f:
        json.dump([], f)

# Load chat history
def load_chat():
    with open(CHAT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Save chat history
def save_chat(messages):
    with open(CHAT_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=4, ensure_ascii=False)

# -----------------------------
# LOAD MEMORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = load_chat()

# -----------------------------
# UI
# -----------------------------
st.title("Memory Chatbot using Groq")

# Display previous chats
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------------
# USER INPUT
# -----------------------------
prompt = st.chat_input("Ask anything...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.write(prompt)

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Limit context (important)
    recent_messages = st.session_state.messages[-30:]

    # Send to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=recent_messages,
        temperature=0.7
    )

    answer = response.choices[0].message.content

    # Show bot answer
    with st.chat_message("assistant"):
        st.write(answer)

    # Save assistant answer
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Save to file
    save_chat(st.session_state.messages)
