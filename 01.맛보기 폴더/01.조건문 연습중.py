import requests
from bs4 import BeautifulSoup

response = requests.get("https://startcoding.pythonanywhere.com/basic")
html = response.text
soup = beautifulsoup(html, 'html.parser')
