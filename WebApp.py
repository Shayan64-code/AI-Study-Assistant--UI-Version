import streamlit as st
from openai import OpenAI
import Keys

st.set_page_config(page_title="Study Assistant", page_icon="📚")
st.title("📚 AI Study Assistant")

client = OpenAI(base_url= "https://openrouter.ai/api/v1",
                api_key=Keys.KEY1)

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system", "content" : ("You are a kindful study assistant. "
                "You tell them all the important points to memorize for exam. "
                "You also solve their code related problems in easy way.")
    }]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

prompt = st.chat_input("Ask your question related to study...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                chats = client.chat.completions.create(
                    model= "nvidia/nemotron-3-nano-30b-a3b:free",
                    messages= st.session_state.messages,
                    temperature= 0.5,
                    max_tokens= 400
                )
                reply = chats.choices[0].message.content
                st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})
        

    except Exception as e:
        st.error(f"Error: {e}")