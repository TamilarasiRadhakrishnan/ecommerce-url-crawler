import re
import requests
from bs4 import BeautifulSoup

def fetch_html(domain):
    """
    Fetch HTML content of the given domain.
    """
    try:
        response = requests.get(domain, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {domain}: {e}")
        return None

def extract_product_urls(html, domain):
    """
    Extract product URLs based on common patterns.
    """
    soup = BeautifulSoup(html, 'html.parser')
    product_urls = set()
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if re.search(r'/product/|/item/|/p/', href):
            if not href.startswith('http'):
                href = domain.rstrip('/') + '/' + href.lstrip('/')
            product_urls.add(href)
    return product_urls
