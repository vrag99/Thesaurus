from bs4 import BeautifulSoup 
import requests 

word = input("Enter a word: ").strip()

search_url = "https://thesaurus.yourdictionary.com/" + word.lower()
response = requests.get(search_url)
soup = BeautifulSoup(response.content , features = 'html.parser')

l = soup.find_all('a', {'class': 'synonym-link'})[:8]

[print(synonym.text) for synonym in l]