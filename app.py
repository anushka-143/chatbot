import os
import streamlit as st
from dotenv import load_dotenv
from scrape import scrape_website
from chatbot import Chatbot

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

chatbot = Chatbot(api_key=openai_api_key)

def main():
    st.title("Website-Based Chatbot")

    url = st.text_input("Enter the URL of the website:", "")
    question = st.text_input("Ask a question about the website content:", "")

    if st.button("Submit"):
        if url and question:
            content = scrape_website(url)
            if content.startswith("Error scraping website:"):
                st.error(content)
            else:
                answer = chatbot.generate_response(question, content)
                st.write("Answer:")
                st.write(answer)
        else:
            st.write("Please enter both a URL and a question.")

if __name__ == "__main__":
    main()
