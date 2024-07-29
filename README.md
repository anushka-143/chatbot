# Website-Based Chatbot

This project is a website-based chatbot that scrapes content from a given URL and uses OpenAI's GPT-3.5-turbo to answer questions based on the scraped content.
## Setup Instructions

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
