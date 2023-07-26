from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from healthfirstai_prototype.chat_agent import init_agent
import streamlit as st

st.set_page_config(page_title="HealthFirst AI: Nutrition Agent Chat", page_icon="❤️")
st.title("❤️ HealthFirst AI: Nutrition Agent Chat")

# openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Type something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=True)
        print(st.session_state.messages[-1]["content"])
        diet_agent = init_agent(
            user_input=st.session_state.messages[-1]["content"],
            user_id=1,
            session_id="streamlit-session",
        )
        response = diet_agent.run(st.session_state.messages[-1]["content"], callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
