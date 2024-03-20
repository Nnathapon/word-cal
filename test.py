from urllib.request import urlopen
from urllib.parse import quote

url = "https://google.com/search/" + quote("ปากกา")
page = urlopen(url)
