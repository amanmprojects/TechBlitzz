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

# Add a debug message after page config
st.write("Debug - App started")

# Load styles
try:
    load_styles()
    st.write("Debug - Styles loaded successfully")
except Exception as e:
    st.error(f"Error in load_styles: {str(e)}")

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    try:
        system_message = get_system_message()
        st.session_state.messages = [system_message]
        st.write("Debug - Session state initialized with system message")
    except Exception as e:
        st.error(f"Error initializing session state: {str(e)}")
        st.session_state.messages = []

# Display UI elements
try:
    display_header()
    display_info_box()
    display_chat_history(st.session_state.messages)
    st.write("Debug - UI elements displayed successfully")
except Exception as e:
    st.error(f"Error displaying UI elements: {str(e)}")

# Handle user input
user_input = get_user_input()
    
if user_input:
    st.write(f"Debug - Received user input: {user_input}")
    
    # Add user message to chat history
    st.session_state.messages.append(HumanMessage(content=user_input))
    
    # Display user message
    display_chat_message(user_input, "user")
    
    # Get AI response
    try:
        chat = get_groq_client()
        st.write("Debug - Groq client initialized")
        
        with st.spinner("Thinking..."):
            st.write("Debug - Sending request to Groq API")
            response = chat.invoke(st.session_state.messages)
            st.write(f"Debug - Got response from Groq API: {type(response)}")
            
            if hasattr(response, 'content'):
                st.write(f"Debug - Response content type: {type(response.content)}")
                st.write(f"Debug - Response content preview: {response.content[:50] if response.content else 'Empty'}")
            else:
                st.write(f"Debug - Response has no content attribute: {response}")
        
        # Clean the response content before storing and displaying
        if hasattr(response, 'content') and response.content:
            cleaned_content = clean_response(response.content)
            
            # Create a new AIMessage with cleaned content
            cleaned_response = AIMessage(content=cleaned_content)
            
            # Add cleaned AI response to chat history
            st.session_state.messages.append(cleaned_response)
            
            # Display AI response
            print(f"Debug - Displaying AI response: {cleaned_content}")
            display_chat_message(cleaned_content, "bot")
        else:
            st.error("Received empty response from the model")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.write(f"Debug - Error details: {traceback.format_exc()}")

# Display footer
setup_footer()