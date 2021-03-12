from bs4 import BeautifulSoup 
import requests 
import keyboard
import os

def get_current_word():
    return keyboard.get_typed_strings(keyboard.record(until='space'))

while True:
    word = list(get_current_word())[0].strip()

    if word.isalpha():

        search_url = "https://thesaurus.yourdictionary.com/" + word.lower()
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content , features = 'html.parser')

        synonyms = soup.find_all('a', {'class': 'synonym-link'})[:5]

        if len(synonyms) != 0:
            print("Synonyms for", word, "==>")
            [print("-", synonym.text) for synonym in synonyms]
            print()

        else:
            print(f"Sorry, nothing matched for '{word}'")
            print()