import requests 
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# Missing closing parenthesis here:
page = requests.get('https://www.billboard.com/charts/hot-100/2025-02-22/', headers=headers)
print(page)
soup = BeautifulSoup(page.text, 'html.parser')
data = []
for e in soup.find_all(attrs={'class':'o-chart-results-list-row'}):
    data.append({
        'title':e.h3.get_text(strip=True),
        'author':e.h3.find_next('span').get_text(strip=True)
    })


print(data)
