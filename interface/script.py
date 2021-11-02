import json
import requests
import streamlit as st


if "conversation" not in st.session_state:
    st.session_state["conversation"] = json.dumps([])

address = st.sidebar.text_input("Address of the chatbot", "http://167.99.12.243:1000/converse")
replies = json.loads(st.session_state["conversation"])

st.title("Interactive Chatbot Tool")
st.write("This is a simple streamlit app to converse with a chatbot.")
st.caption("Conversation")


if len(replies) == 0:
    st.info("The conversation is currently empty, replies will appear here.")
else:
    for i, reply in enumerate(replies):
        actor = "User" if i % 2 == 0 else "Bot"
        st.write(f"{actor}: {reply}")


st.text("")
reply = st.text_input("Type something...")


def ask_model(utterances):
    r = requests.post(address, json={"utterances": utterances})
    return r.json()
    

def reply_callback(reply):
    if len(reply.strip()) > 0:
        utterances = replies + [reply]
        with st.spinner('Waiting for model...'):
            reply = ask_model(utterances)
        st.session_state["conversation"] = json.dumps(utterances + [reply])
        reply = ""


clicked = st.button("Send", args=(reply,), on_click=reply_callback)
