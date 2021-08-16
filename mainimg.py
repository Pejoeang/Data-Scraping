import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

url = 'https://store.steampowered.com/games#p=0&tab=NewReleases'

r=requests.get (url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
new_releases = soup.find('div', attrs={'id','tab_newreleases_content'})
newReleasesContents= soup.findAll('a', attrs={'class':'tab_item'})

for newReleasesContent in newReleasesContents:
    imageUrl=newReleasesContent.find('img', attrs={'class','tab_item_cap_img'})['src']
    titles = newReleasesContent.find('div', attrs={'class','tab_item_name'}).text
    response = requests.get(imageUrl, headers=headers, stream=True)
    fileName = imageUrl.split("/")[-1].split("?")[0]
    ext = fileName[-4:]
    if response.ok:
        with open('images/' + re.sub(r'(?u)[^-\w.]', '_', titles) + ext, 'wb') as a:
            a.write(response.content)