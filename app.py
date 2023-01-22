import requests
from bs4 import BeautifulSoup as bs

url = "https://mengxian0913.github.io/VincentLily/"

response = requests.get(url)
soup = bs(response.content, "html.parser")
img_tags = soup.find_all("img")
img_urls = [img["src"] for img in img_tags]

import json

json_imgs = []

for i in img_urls:
    json_imgs.append(i)



from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.debug = True
    app.run()