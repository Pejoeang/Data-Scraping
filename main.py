import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def top_sellers():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    url = 'https://store.steampowered.com/games/TopSellers#p=0&tab=TopSellers'
    r = requests.get(url, headers=headers)
    #print(r)
    soup=BeautifulSoup(r.text, 'html.parser')
    top_sellers=soup.findAll('a', attrs={'class':'tab_item'})
    return render_template('grid_template.html', top_sellers=top_sellers)

if __name__ == "__main__":
    app.run(debug=True)



for top_seller in top_sellers:
    print('Tittles: ', top_seller.find('div', attrs={'class':'tab_item_name'}).text)
    print('Images: ', top_seller.find('div', attrs={'class':'tab_item_cap'}).find('img'))
    print('Tags: ', top_seller.find('div', attrs={'class':'tab_item_top_tags'}).text)
