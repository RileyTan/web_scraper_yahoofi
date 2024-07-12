import requests
import lxml.html

html = requests.get("https://sg.finance.yahoo.com/quote/DIS/key-statistics/")
doc = lxml.html.fromstring()
