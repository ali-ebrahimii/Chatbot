import streamlit as st
from src.main import call_Orca_Mini

st.title('💬 Orca Mini (3B :llama: Ollama) Chatbot')
st.caption("🚀 A streamlit chatbot powered by Orca Mini LLM")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner('Generating response...'):
        msg = call_Orca_Mini('orca-mini', prompt)['response']
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)