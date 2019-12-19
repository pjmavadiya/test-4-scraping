from bs4 import BeautifulSoup
import requests


def get_follower(url):

    page_data = requests.get(url)
    bs = BeautifulSoup(page_data.text)
    try:
        follow_area = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
        temp = follow_area.find('a')
        followers = temp.find('span',{'class':'ProfileNav-value'})
        
        follow_area = bs.find('h1','ProfileHeaderCard-name')
        name = follow_area.find('a').text
        
        return followers.get('data-count'), name
    except:
        return 'Please enter valid URL.', None