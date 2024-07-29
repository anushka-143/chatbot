# Chatbot Project

## Overview

This project is a chatbot application that uses OpenAI's GPT-3.5-turbo model to generate responses based on context and user queries. The chatbot is designed to handle input and provide meaningful answers based on data scraped from a specified website.

## Features

- Scrapes website content using BeautifulSoup.
- Generates responses using OpenAI's GPT-3.5-turbo model.
- Provides a command-line interface for interaction.

## Requirements

- Python 3.8 or higher
- `openai` library
- `beautifulsoup4` library
- `requests` library

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
https://github.com/anushka-143/chatbot.git

### Step 1: Create and activate a virtual environment

#### Using Conda
```bash
conda env create -f environment.yml
conda activate chatbot_project

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# create an .env file and add your openAI API key
OPENAI_API_KEY=your_openai_api_key_here

# run the streamlit code using terminal
streamlit run app.py
