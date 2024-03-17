
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_gmb_listing(url):
                                    
    response = requests.get(url) # Send request to URL and get response
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    gmb_details = {}
    
    # Extract
    gmb_details['Name'] = soup.find('span', class_='LrzXr').text.strip() if soup.find('span', class_='LrzXr') else ''
    gmb_details['Address'] = soup.find('span', class_='LrzXr').text.strip() if soup.find('span', class_='LrzXr') else ''
    gmb_details['Phone'] = soup.find('span', class_='zdqRlf').text.strip() if soup.find('span', class_='zdqRlf') else ''
    gmb_details['Website'] = soup.find('div', class_='QqG1Sd').a['href'] if soup.find('div', class_='QqG1Sd') else ''
    
    return gmb_details

# Example usage
url = 'https://www.google.com/search?q=local+business'
details = scrape_gmb_listing(url)
print(details)
