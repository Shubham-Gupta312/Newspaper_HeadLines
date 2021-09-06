import requests
import json
def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)


if __name__ == '__main__':
    speak("Namaskar! Todays, News Headlines")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=2f22dae4e83b484b9cccd6acd92f54af"

    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict["articles"])

    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving to the Next News")
        speak("Listen Carefully!")




