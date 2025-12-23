import streamlit as st
import json
import os

CHAT_FILE = "chat_history.json"
client = OpenAI(api_key="YOUR_API_KEY")

st.set_page_config(page_title="Persistent LLM Chat", layout="centered")
st.title("🧠 Persistent LLM Chat")

def load_chat():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as f:
            return json.load(f)
    return [
        {"role": "system", "content": "You are a helpful assistant."}
    ]


def save_chat(messages):
    with open(CHAT_FILE, "w") as f:
        json.dump(messages, f, indent=2)

if "messages" not in st.session_state:
    st.session_state.messages = load_chat()


for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        answer = response.choices[0].message.content
        st.markdown(answer)

  
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    
    save_chat(st.session_state.messages)

if st.button("🗑️ Clear Chat History"):
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    save_chat(st.session_state.messages)
    st.rerun()
