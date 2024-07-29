import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p') 
        content = ' '.join([p.get_text() for p in paragraphs])
        return content
    except requests.exceptions.RequestException as e:
        return f"Error scraping website: {e}"
