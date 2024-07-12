import requests
import lxml.html

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
html = requests.get("https://sg.finance.yahoo.com/quote/DIS/key-statistics/", headers=headers)
# fromstring() expects a string. html.content is the string
doc = lxml.html.fromstring(html.text)

# if making a web-based API, JSON as output is better choice, easily consumed by more prog languages
# if planning to do data analysis/manipulation, CSV might be more suitable, can import into Excel
valuation_measures = doc.xpath('//div[@id="Col1-0-KeyStatistics-Proxy"]')[0]

measure_names = valuation_measures.xpath('.//)
