import requests
from bs4 import BeautifulSoup

url = 'https://www.republicworld.com/india'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    tags = soup.find_all(['h1', 'h2', 'title'])
    headlines = set()  

    for tag in tags:
        text = tag.get_text(strip=True)
        if text and len(text) > 10:  
            headlines.add(text)

    
    with open('news_headlines.txt', 'w', encoding='utf-8') as f:
        for headline in headlines:
            f.write(headline + '\n')

    print(f"{len(headlines)} headlines saved to 'news_headlines.txt'")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
