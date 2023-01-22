import requests
from bs4 import BeautifulSoup as bs

url = "https://www.instagram.com/kurosaki0516/"

response = requests.get(url)
# real_url = response.headers["Location"]
soup = bs(response.content, "html.parser")
img_tags = soup.find_all("img")
img_urls = [img["src"] for img in img_tags]

for i in img_urls:
    print(i)