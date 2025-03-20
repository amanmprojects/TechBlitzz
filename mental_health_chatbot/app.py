import streamlit as st
from dotenv import load_dotenv
from langchain.schema import HumanMessage, AIMessage
import traceback

# Import from local modules
from config import load_styles, setup_footer
from model import get_groq_client, get_system_message
from ui import display_header, display_info_box, display_chat_history, display_chat_message, get_user_input
from utils import clean_response

# Set page config - MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Mental Health Assistant",
    page_icon="🧠",
    layout="wide",
)

# Load environment variables
load_dotenv()

# Load styles
try:
    load_styles()
except Exception as e:
    st.error(f"Error in load_styles: {str(e)}")

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    try:
        system_message = get_system_message()
        st.session_state.messages = [system_message]
    except Exception as e:
        st.error(f"Error initializing session state: {str(e)}")
        st.session_state.messages = []

# Display UI elements
try:
    display_header()
    display_info_box()
    display_chat_history(st.session_state.messages)
except Exception as e:
    st.error(f"Error displaying UI elements: {str(e)}")

# Handle user input
user_input = get_user_input()
    
if user_input:
    # Add user message to chat history
    st.session_state.messages.append(HumanMessage(content=user_input))
    
    # Display user message
    display_chat_message(user_input, "user")
    
    # Get AI response
    try:
        chat = get_groq_client()
        
        with st.spinner("Thinking..."):
            response = chat.invoke(st.session_state.messages)
        
        # Clean the response content before storing and displaying
        if hasattr(response, 'content') and response.content:
            cleaned_content = clean_response(response.content)
            
            # Create a new AIMessage with cleaned content
            cleaned_response = AIMessage(content=cleaned_content)
            
            # Add cleaned AI response to chat history
            st.session_state.messages.append(cleaned_response)
            
            # Display AI response
            display_chat_message(cleaned_content, "bot")
        else:
            st.error("Received empty response from the model")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Display footer
setup_footer()