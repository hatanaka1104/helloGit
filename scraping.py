import requests
from bs4 import Beautiful Soup
pageurl =""

r = requests.get(pageurl)
soup=BeautifulSoup(r.text,html.parser)