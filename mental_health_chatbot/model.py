import os
from typing import Optional
import streamlit as st
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, BaseMessage

# Constants
MODEL_NAME = "deepseek-r1-distill-llama-70b"
TEMPERATURE = 0.5
MAX_TOKENS = 1000

def get_groq_client() -> ChatGroq:
    """
    Initialize and return the Groq LLM client.
    
    Returns:
        ChatGroq: Configured Groq client instance
        
    Raises:
        ValueError: If GROQ_API_KEY is not found in environment variables
    """
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        error_msg = "GROQ_API_KEY not found in environment variables. Please set it in the .env file."
        st.error(error_msg)
        raise ValueError(error_msg)
    
    return ChatGroq(
        api_key=groq_api_key,
        model_name=MODEL_NAME,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

def get_system_message() -> SystemMessage:
    """
    Return the system message that defines the AI assistant's behavior.
    
    Returns:
        SystemMessage: Configured system message for the AI assistant
    """
    return SystemMessage(content="""
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

Remember to:
- Use appropriate language and tone for the context
- Provide specific, actionable advice when possible
- Include relevant resources and references when appropriate
- Maintain professional boundaries while being supportive
- Acknowledge the user's feelings and experiences
""")