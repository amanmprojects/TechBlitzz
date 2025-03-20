from typing import NoReturn
import streamlit as st

def load_styles() -> NoReturn:
    """
    Load custom CSS styles for the chat interface.
    
    This function injects custom CSS into the Streamlit app to style the chat interface,
    including message bubbles, avatars, and overall theme.
    """
    st.markdown("""
<style>
    /* Main app styling */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* Chat message container */
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.8rem;
        margin-bottom: 1rem;
        display: flex;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease;
    }
    
    .chat-message:hover {
        transform: translateY(-2px);
    }
    
    /* User message styling */
    .chat-message.user {
        background-color: #e0f7fa;
        color: #006064;
        border-left: 4px solid #00bcd4;
    }
    
    /* Bot message styling */
    .chat-message.bot {
        background-color: #ffebee;
        color: #c62828;
        border: 1px solid #ffcdd2;
        border-left: 4px solid #ef5350;
    }
    
    /* Avatar styling */
    .chat-message .avatar {
        width: 40px;
        height: 40px;
        margin-right: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    /* Message content styling */
    .chat-message .message {
        flex-grow: 1;
        line-height: 1.5;
    }
</style>
    """, unsafe_allow_html=True)

def setup_footer() -> NoReturn:
    """
    Display the footer with disclaimer and additional information.
    
    This function creates a footer section with a disclaimer about the nature
    of the mental health assistant and its limitations.
    """
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 1rem;">
            <p style="color: #888; font-size: 0.8rem; margin: 0;">
                This assistant is for informational purposes only. 
                Always consult with qualified mental health professionals for medical advice.
            </p>
            <p style="color: #666; font-size: 0.7rem; margin-top: 0.5rem;">
                If you're experiencing a crisis, please contact emergency services immediately.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )