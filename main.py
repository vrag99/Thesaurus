# Importing required modules
from bs4 import BeautifulSoup 
import requests 
import keyboard


def get_current_word():
    ''' 
    Recording the key presses until <space> is pressed,
    i.e. gets the current word typed.
    '''

    return keyboard.get_typed_strings(keyboard.record(until='space'))


# A few phrases that need not be considered for synonym check.
auxillary_phrases = {'is', 'am', 'are', 'has', 'have', 'had', 'been', 'was',
'would', 'should', 'shall', 'may', 'might', 'a', 'an', 'the', 'you', 'we',
'i', 'of', 'will', 'us', 'and'}


# Welcome statement
print("Hey, I am Thesaurus! \nYou can start typing (not in the terminal) and I will display the resp. synonyms here!")


while True:
    word = list(get_current_word())[0].strip().lower()

    # Searching for the word's meaning.
    if word.isalpha() and word not in auxillary_phrases:

        # Scraping the data from the website.
        search_url = "https://thesaurus.yourdictionary.com/" + word
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content , features = 'html.parser')

        # Getting the first '5' synonyms
        synonyms = soup.find_all('a', {'class': 'synonym-link'})[:5]

        if len(synonyms) != 0:
            print(f"Synonyms for '{word}' ==>")
            [print("-", synonym.text) for synonym in synonyms]
            print()

        else:
            print(f"Sorry, nothing matched for '{word}'\n")