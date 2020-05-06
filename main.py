#Akhbaar padhke sunaao
# Attempt it yourself and watch the series for solution and shoutouts for this lecture!
#use newsAPI key, go to newsapi site,register and get your own api and use it in your program

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
   # url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=6d34b621f6d74729a068cd7a9ff70e47"
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=6d34b621f6d74729a068cd7a9ff70e47"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")