from bs4 import *
import requests,Image
from StringIO import StringIO
req=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
brainyreq = BeautifulSoup(req.text,"lxml")
brainymarcus = brainyreq.findAll("img")[2]
marcusimage = "https://www.brainyquote.com" + brainymarcus["src"]
im=Image.open(StringIO(requests.get(marcusimage).content))
im.show()
im.save("Marcus.png")