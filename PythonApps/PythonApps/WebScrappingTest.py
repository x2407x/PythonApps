# C:\Users\doan_\source\repos\x2407x\repos\PythonApps\PythonApps\WebScrappingTest.py
from bs4 import BeautifulSoup
import requests
r = requests.get("http://en.wikipedia.org/wiki/List_of_countries_by_population ")
data = r.text
soup = BeautifulSoup(data, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))