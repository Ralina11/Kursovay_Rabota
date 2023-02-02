from basic_word import BasicWord
import requests
import random

def load_random_word():
    response = requests.get("https://api.npoint.io/e88f87fb963d9ea33f49")
    result = response.json()
    random.shuffle(result)
    word = BasicWord(result[0]["word"], result[0]["subwords"])
    return word

