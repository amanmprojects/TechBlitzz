from typing import List, Optional
import streamlit as st
from langchain.schema import HumanMessage, AIMessage, BaseMessage
from utils import clean_response, format_message, sanitize_input

def display_header() -> None:
    """
    Display the application header and subheader with enhanced styling.
    """
    st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <h1 style="color: #00bcd4; margin-bottom: 0.5rem;">🧠 Mental Health Assistant</h1>
            <p style="color: #666; font-size: 1.1rem;">A supportive space to talk about your mental health</p>
        </div>
    """, unsafe_allow_html=True)

def display_info_box() -> None:
    """
    Display information about the assistant in an expandable box with enhanced content.
    """
    with st.expander("ℹ️ About this assistant", expanded=False):
        st.markdown("""
        ### Welcome to your Mental Health Assistant
        
        This AI-powered assistant is designed to provide support and resources for mental health concerns. 
        Here's what I can help you with:
        
        - 🤝 Discussing feelings and emotions
        - 🧘‍♂️ Providing coping strategies for stress, anxiety, or low mood
        - 🌱 Suggesting relaxation techniques
        - 💡 Offering general mental wellness advice
        
        ### Important Information
        
        ⚠️ **This is not a substitute for professional mental health care.** 
        If you're experiencing a crisis or need immediate help:
        
        - Contact emergency services (911)
        - Call a mental health crisis line
        - Reach out to a mental health professional
        
        ### Privacy & Confidentiality
        
        Your conversations are private and confidential. However, please note that this is an AI assistant
        and should not be used for emergency situations or serious mental health concerns.
        """)

def display_chat_message(message: str, role: str) -> None:
    """
    Display a single chat message with enhanced styling and formatting.
    
    Args:
        message (str): The message content to display
        role (str): The role of the message sender ('user' or 'bot')
    """
    if not message:
        return
        
    formatted_message = format_message(message)
    
    if role == "user":
        st.markdown(f"""
        <div class="chat-message user">
            <div class="avatar">👤</div>
            <div class="message">{formatted_message}</div>
        </div>
        """, unsafe_allow_html=True)
    else:  # bot message
        st.markdown(f"""
        <div class="chat-message bot">
            <div class="avatar">🧠</div>
            <div class="message">{formatted_message}</div>
        </div>
        """, unsafe_allow_html=True)

def display_chat_history(messages: List[BaseMessage]) -> None:
    """
    Display the entire chat history with proper message handling.
    
    Args:
        messages (List[BaseMessage]): List of chat messages to display
    """
    for message in messages[1:]:  # Skip the system message
        try:
            if isinstance(message, HumanMessage):
                display_chat_message(message.content, "user")
            elif isinstance(message, AIMessage):
                cleaned_content = clean_response(message.content)
                display_chat_message(cleaned_content, "bot")
        except Exception as e:
            st.error(f"Error displaying message: {str(e)}")
            continue

def get_user_input() -> Optional[str]:
    """
    Get user input via chat input with enhanced validation.
    
    Returns:
        Optional[str]: The sanitized user input, or None if no input was provided
    """
    user_input = st.chat_input("How are you feeling today?")
    
    if user_input:
        return sanitize_input(user_input)
    return None