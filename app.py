import streamlit as st
import os
import re
from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="Mental Health Assistant",
    page_icon="🧠",
    layout="wide",
)

# Customize the appearance
st.markdown("""
<style>
    .stApp {
        background-color: #f5f7fd;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.8rem;
        margin-bottom: 1rem;
        display: flex;
    }
    /* Updated user message colors: light blue background with dark teal text */
    .chat-message.user {
        background-color: #e0f7fa;
        color: #006064;
    }
    /* Updated bot message colors: light red background with deep red text and a clearer border */
    .chat-message.bot {
        background-color: #ffebee;
        color: #c62828;
        border: 1px solid #ffcdd2;
    }
    .chat-message .avatar {
        width: 40px;
        margin-right: 10px;
    }
    .chat-message .message {
        flex-grow: 1;
    }
</style>

""", unsafe_allow_html=True)

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="""
You are a supportive, empathetic mental health assistant designed to provide 
guidance, resources, and a compassionate ear. You're here to support patients 
with their mental health concerns, offer coping strategies, and provide a 
safe space for them to express their feelings.

Important guidelines:
- Always be kind, patient, and empathetic
- Never diagnose medical conditions
- Emphasize that you're not a replacement for professional mental health care
- Encourage seeking professional help for serious concerns
- Focus on evidence-based coping strategies and wellness techniques
- Provide emotional support without judgment
- Respect patient privacy and confidentiality
- Use clear, non-technical language when possible
- Be cautious with advice and emphasize personal agency

If someone expresses thoughts of self-harm or suicidal ideation, gently encourage 
them to contact emergency services, a crisis hotline, or their healthcare provider immediately.
""")
    ]

# Function to clean response - remove <think> </think> tags and their content
def clean_response(response_text):
    # Remove content between <think> and </think> tags, including the tags
    cleaned_text = re.sub(r'<think>.*?</think>', '', response_text, flags=re.DOTALL)
    return cleaned_text.strip()

# Initialize Groq client
@st.cache_resource
def get_groq_client():
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        st.error("GROQ_API_KEY not found in environment variables. Please set it in the .env file.")
        st.stop()
    
    return ChatGroq(
        api_key=groq_api_key,
        model_name="deepseek-r1-distill-llama-70b",
        temperature=0.5,
        max_tokens=1000
    )

# Header
st.title("🧠 Mental Health Assistant")
st.subheader("A supportive space to talk about your mental health")

# Information box
with st.expander("ℹ️ About this assistant", expanded=False):
    st.markdown("""
    This assistant is designed to provide support and resources for mental health concerns. 
    It can help with:
    
    - Discussing feelings and emotions
    - Providing coping strategies for stress, anxiety, or low mood
    - Suggesting relaxation techniques
    - Offering general mental wellness advice
    
    **Important:** This is not a substitute for professional mental health care. 
    If you're experiencing a crisis or need immediate help, please contact emergency services 
    or a mental health crisis line.
    """)

# Display chat history
for message in st.session_state.messages[1:]:  # Skip the system message
    if isinstance(message, HumanMessage):
        st.markdown(f"""
        <div class="chat-message user">
            <div class="avatar">👤</div>
            <div class="message">{message.content}</div>
        </div>
        """, unsafe_allow_html=True)
    elif isinstance(message, AIMessage):
        # Clean the message content before displaying
        cleaned_content = clean_response(message.content)
        st.markdown(f"""
        <div class="chat-message bot">
            <div class="avatar">🧠</div>
            <div class="message">{cleaned_content}</div>
        </div>
        """, unsafe_allow_html=True)

# Chat input
with st.container():
    user_input = st.chat_input("How are you feeling today?")
    
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append(HumanMessage(content=user_input))
        
        # Display user message
        st.markdown(f"""
        <div class="chat-message user">
            <div class="avatar">👤</div>
            <div class="message">{user_input}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Get AI response
        chat = get_groq_client()
        try:
            with st.spinner("Thinking..."):
                response = chat.invoke(st.session_state.messages)
            
            # Clean the response content before storing and displaying
            cleaned_content = clean_response(response.content)
            
            # Create a new AIMessage with cleaned content
            cleaned_response = AIMessage(content=cleaned_content)
            
            # Add cleaned AI response to chat history
            st.session_state.messages.append(cleaned_response)
            
            # Display AI response
            st.markdown(f"""
            <div class="chat-message bot">
                <div class="avatar">🧠</div>
                <div class="message">{cleaned_content}</div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center">
        <p style="color: #888; font-size: 0.8rem;">
            This assistant is for informational purposes only. 
            Always consult with qualified mental health professionals for medical advice.
        </p>
    </div>
    """, 
    unsafe_allow_html=True)