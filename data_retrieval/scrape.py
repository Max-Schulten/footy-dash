# Scraping script to pull historical results for 'major european leagues'. Source: (https://www.football-data.co.uk/data.php)

# Declaration of Constants
BASE_URL = "https://www.football-data.co.uk" 
HOME_URL = f"{BASE_URL}/data.php"

# HTML parser
from bs4 import BeautifulSoup
# HTML requests
import requests as req
# Pandas...
import pandas as pd
# Regex
import re

# Scrapes a league's page
def scrape_league_page(url: str, session: req.Session) -> bool:
    
    # Fetch HTML from url
    page_html = session.get(url)
    

def leagues_nav(url: str, session: req.Session | None = None) -> bool:
    
    # Create session if none exists
    if not session:
        session = req.Session()
        
    # Fetch HTML
    page_request = session.get(url)
    
    # Ensure good response
    if page_request.status_code != 200:
        return False
    
    # Parse HTML
    page_parser = BeautifulSoup(page_request.content, 'html.parser')
    
    header = page_parser.find('p', string=re.compile('Main Leagues', re.IGNORECASE))
    
    table = header.find_next('table')
    
    rows = table.find_all('tr')
    
    for row in rows:
        a_tag = row.find('a')
        league_page = a_tag.get("href")
        print(f"{BASE_URL}/{league_page}")
        
    
    return True

leagues_nav(HOME_URL)