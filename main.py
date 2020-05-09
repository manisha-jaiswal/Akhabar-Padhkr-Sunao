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
  
    url="your upi"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")
