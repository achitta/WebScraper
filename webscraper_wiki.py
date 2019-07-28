from bs4 import BeautifulSoup
import requests
import json

def scrape_degrees(start, end, count, count_fixed):
    print(start)
    print(count)
    if(len(start) < 3) :
        return

    flag = True
    if(count == 1) :
        flag = False
    if(count == 0) :
        return

    url = 'https://en.wikipedia.org/wiki/' + start
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    hyperlinks = []
    limit = 0
    for link in content.findAll('a'):
        if(len(link.text) < 12 and len(link.text) > 2) : 
            if (ord(link.text[0:1]) >= 65 and ord(link.text[0:1]) <= 90) or (ord(link.text[0:1]) >= 97 and ord(link.text[0:1]) <= 122) :
                hyperlinks.append(link.text)
                limit = limit + 1
                if(link.text == end) :
                    print("Path Found!")
                    print(str(count_fixed-count) + " degrees away!")
                    exit(0)
                if(flag) :
                    scrape_degrees(link.text, end, count - 1, count_fixed)
                    print("Back to " + start)
                if(limit > 50) :
                    print("Reached Limit")
                    return
    print("Length of Array for " + start + ": " + str(len(hyperlinks))) 
    print('\n')
        
    with open('wikiData.json', 'w') as fp:
        json.dump(hyperlinks, fp, indent=3)

    with open('wikiData.json') as json_file:
        data = json.load(json_file)


def scrape_func(start) :
    url = 'https://en.wikipedia.org/wiki/' + start
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    hyperlinks = []
    for link in content.findAll('a'):
        if(len(link.text) < 12 and len(link.text) > 2) : 
            if (ord(link.text[0:1]) >= 65 and ord(link.text[0:1]) <= 90) or (ord(link.text[0:1]) >= 97 and ord(link.text[0:1]) <= 122) :
                hyperlinks.append(link.text)
    print("Length of Array for " + start + ": " + str(len(hyperlinks))) 
    
    
    with open('wikiData.json', 'w') as fp:
        json.dump(hyperlinks, fp, indent=3)

    with open('wikiData.json') as json_file:
        data = json.load(json_file)

starting_topic = input("Enter Starting Topic: ")
ending_topic = input("Enter Ending Topic: ")
degrees = int(input("Enter number of degrees: "))

scrape_degrees(starting_topic, ending_topic, degrees, degrees+1)
# scrape_func("Monkey")