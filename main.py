from bs4 import BeautifulSoup
import requests

url = 'https://iqflynncybersecurity.com'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
