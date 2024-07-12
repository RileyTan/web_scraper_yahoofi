import requests
import lxml.html

html = requests.get("https://sg.finance.yahoo.com/quote/DIS/key-statistics/")
# fromstring() expects a string. html.content is the string
doc = lxml.html.fromstring(html.text)

# if making a web-based API, JSON as output is better choice, easily consumed by more prog languages
# if planning to do data analysis/manipulation, CSV might be more suitable, can import into Excel

