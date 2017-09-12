from html.parser import HTMLParser
from bs4 import BeautifulSoup
import urllib.request

class ParseThis(HTMLParser):
    def handle_data(self, data):
        print(data.replace(',', '').replace('[','').replace(']',''))


url = "https://www.fanfiction.net/s/11290820/1/ZELDA-AND-SONIC-S-DAY-OUT"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content)

parser = ParseThis()
parser.feed(str(soup.find_all('p')))
