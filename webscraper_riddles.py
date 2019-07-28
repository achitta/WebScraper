from bs4 import BeautifulSoup
import requests
import json
def scrape_riddle_site() :
    q_url = 'https://www.braingle.com/brainteasers/teaser.php?rand=1'
    q_response = requests.get(q_url, timeout=5)
    q_content = BeautifulSoup(q_response.content, "html.parser")

    riddle = q_content.find('div', attrs={"class": "textblock"}).text
    
    full_answer_link = str(q_content.find('a', attrs={"class": "space_right ans_h button_primary t1"}))
    answer_url_part_two =  convert_tag_to_url(full_answer_link)
    answer_url = "https://www.braingle.com/" + answer_url_part_two

    a_url = answer_url
    a_response = requests.get(a_url, timeout=5)
    a_content = BeautifulSoup(a_response.content, "html.parser")

    answer = a_content.find('div', attrs={"class": "ans_s"}).text

    x = {"Question":riddle, "Answer":answer}

    print(riddle)
    print('\n')
    print(answer)

    with open('riddle.json', 'w') as fp:
        json.dump(x, fp, indent=3)

def convert_tag_to_url(full_tag) :
    href_num = full_tag.find("href=")
    closing_num = full_tag.find(">")
    sub_tag = full_tag[href_num+7:closing_num-1]
    url = sub_tag.replace("&amp;","&")
    return url

scrape_riddle_site() 