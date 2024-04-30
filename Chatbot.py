import streamlit as st
from langchain import HuggingFaceHub
import os



model_id = "mistralai/Mistral-7B-Instruct-v0.2"

# Set up Hugging Face model with increased max_new_tokens
conv_model = HuggingFaceHub(huggingfacehub_api_token="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",
                            repo_id=model_id,
                            model_kwargs={"temperature": 0.6, "max_new_tokens": 5000})  # Increase response length here

# Define function to generate chat response
def generate_response(query):
    try:
        # Define responses to specific questions
        specific_responses = {
            "what is your name?": "I am an AI based Chatbot created by Team Clueless Coders ",
            "hi": "How can I help you?",
            "what is your use case?": "You can count on me to answer any of your career related questions.",
            # Add more specific questions and responses here
        }
        
        # Check if the query is a specific question with predefined response
        if query.lower() in specific_responses:
            return specific_responses[query.lower()]
        # Otherwise, use the model to generate a response
        else:
            return conv_model(query)
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return ""

# Streamlit UI
def main():
    st.title("DestiNation Bot")

    
    # Initialize chat history as empty list
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    query = st.text_input("Enter your carrier related query:")
    submit_button_placeholder = st.empty()  # Placeholder for submit button
    
    if st.button("Submit", key="submit_button") and query:
        bot_response = generate_response(query)
        st.session_state.chat_history.append({"user": query, "bot": bot_response})
    
    if st.session_state.chat_history:
        conversation_history = ""
        for item in st.session_state.chat_history:
            conversation_history += "🧑🏻‍💻: " + item["user"] + "\n🤖: " + item["bot"] + "\n\n"
        
        st.text_area("Conversation :", value=conversation_history.strip(), height=400)

    # Align the submit button with the text area
    st.markdown('<style>div.stButton > button {width: 100%;}</style>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
