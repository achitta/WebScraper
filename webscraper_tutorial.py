from bs4 import BeautifulSoup
import requests
import json
url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": (tweet.find('h2', attrs={"class": "author"}).text),
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class": "content"}).text,
        "likes": tweet.find('p', attrs={"class": "likes"}).text,
        "shares": tweet.find('p', attrs={"class": "shares"}).text
    }
    tweetArr.append(tweetObject)

with open('twitterDataTutorial.json', 'w') as fp:
    json.dump(tweetArr, fp, indent=3)

with open('twitterDataTutorial.json') as json_file:
    data = json.load(json_file)

count = 1
for obj in data:
    if(int(obj["shares"][8:]) > 10000):
        print(obj["tweet"])
        print("Count: " + str(count))
        count = count + 1
        print('\n')
