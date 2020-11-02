""""
Scheme:
1. Create class for a card
2. Scrape information and then make Card instances
3. Display information in an editable format
    3a. Find way to include images in the information
    3b. 
4. When user submits, convert the entire thing into an exportable format
5. User must create and then import that text into another quizlet set
"""

from PIL import Image
import requests
import urllib
from io import BytesIO
import bs4

class Card:

    def __init__(self, term, definition, number, image_given=None):
        self.term = term
        self.definition = definition
        self.term_number = str(number)
        # if you get a link for an image, get the image and save it under self.image
        if image_given is not None:
            try:
                image_request = requests.get(image)
            except:
                self.image = None
                self.image_bool = False
            else:
                self.image = Image.open(BytesIO(image_request.content))
                self.image_bool = True

    def add_image(self, image):
        pass

    def __str__(self):
        return self.term + ": " + self.definition

def get_quizlet_set(url):
    # acquire quizlet set and turn into soup
    # quizlet_url = input("Please paste the link to the Quizlet set you'd like to edit: ")
    quizlet_url = url
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    q_request = requests.get(quizlet_url, headers=headers)
    soup = bs4.BeautifulSoup(q_request.text, 'lxml')
    return soup

def find_terms(soup):
    quizlet_info = soup.find_all('span', class_='TermText notranslate lang-en')
    quizlet_cards = []
    card_num = 1
    for counter in range(0, len(quizlet_info)-1, 2):
        quizlet_cards.append(Card(quizlet_info[counter].text, quizlet_info[counter + 1].text, card_num))
        card_num += 1
    return quizlet_cards