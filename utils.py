import re
from typing import Optional
import streamlit as st

def clean_response(response_text: Optional[str]) -> str:
    """
    Clean and format the response text by removing unwanted tags and formatting.
    
    Args:
        response_text (Optional[str]): The raw response text to clean
        
    Returns:
        str: Cleaned and formatted response text
        
    Note:
        This function removes content between <think> tags and performs basic text formatting.
    """
    if not response_text:
        return ""
    
    # Remove content between <think> and </think> tags, including the tags
    cleaned_text = re.sub(r'<think>.*?</think>', '', response_text, flags=re.DOTALL)
    
    # Additional cleaning steps
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Normalize whitespace
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text

def format_message(message: str, max_length: int = 1000) -> str:
    """
    Format a message to ensure it's within length limits and properly formatted.
    
    Args:
        message (str): The message to format
        max_length (int, optional): Maximum length of the message. Defaults to 1000.
        
    Returns:
        str: Formatted message
    """
    if not message:
        return ""
    
    # Truncate if too long
    if len(message) > max_length:
        message = message[:max_length] + "..."
    
    return message.strip()

def sanitize_input(user_input: str) -> str:
    """
    Sanitize user input to prevent potential security issues.
    
    Args:
        user_input (str): Raw user input
        
    Returns:
        str: Sanitized user input
    """
    if not user_input:
        return ""
    
    # Remove potentially harmful HTML/script tags
    sanitized = re.sub(r'<[^>]+>', '', user_input)
    
    # Remove multiple spaces and trim
    sanitized = re.sub(r'\s+', ' ', sanitized).strip()
    
    return sanitized