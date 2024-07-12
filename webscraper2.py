import requests
import lxml.html

html = requests.get("https://sg.finance.yahoo.com/quote/DIS/key-statistics/")
# fromstring() expects a string. html.content is the string
doc = lxml.html.fromstring(html.text)

