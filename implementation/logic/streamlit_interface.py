import streamlit as st
import langchain_core

from config import OPEN_AI_APIKEY, SYSTEM_PROMPT
from langchain_openai.chat_models import ChatOpenAI
from langchain.agents import create_agent
from fetch_order_information import fetch_order_by_email, fetch_order_by_id
from langchain.tools import tool

import asyncio

st.set_page_config(page_title="GT Ecom - Customer Support")
st.title("Order information and customer service ")
st.markdown("#### Got any questions regarding your order? Our agent will happily answer them for you.")

if "history" not in st.session_state:
    st.session_state.history = []  

llm = ChatOpenAI(
    model="gpt-5",
    temperature=0.5,
)

@tool
def get_order_by_id(order_id: str) -> dict:
    """
    Fetch an order by id from a provided csv table.
    """
    return fetch_order_by_id(order_id)

@tool
def get_order_by_email(email: str) -> dict:
    """
    Fetch an order by email from a provided csv table.
    """
    return fetch_order_by_email(email)

agent = create_agent(system_prompt=SYSTEM_PROMPT, 
                     tools=[get_order_by_email, get_order_by_id], 
                     model=llm)

async def generate_response(input_text):
    message_from_model = await agent.ainvoke({"messages": st.session_state.history})
    return message_from_model


user_input = st.chat_input("Say something...")

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        #Using asyncio, since the generated API key can only be used with asynchronous operations
        response = asyncio.run(generate_response(user_input))
        latest_ai_message = response["messages"][-1].content
        st.write(latest_ai_message)
        
        #save models responses as well for a complete chat history
        st.session_state.history.append({"role": "assistant", "content": latest_ai_message})
