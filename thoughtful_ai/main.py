import streamlit as st
from agent import ThoughtfulAIAgent

agent = ThoughtfulAIAgent()

st.set_page_config(page_title="Thoughtful AI Support Agent", page_icon="🤖")
st.title("🤖 Thoughtful AI Support Agent")
st.write("Ask anything about Thoughtful AI's agents or general questions!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def send_message():
    user_input = st.session_state.user_input
    if not user_input.strip():
        return
    response = agent.get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Agent", response))
    st.session_state.user_input = ""

st.text_input("You:", key="user_input", on_change=send_message)

for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Agent:** {message}")
