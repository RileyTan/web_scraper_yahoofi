import requests
import lxml.html
import json

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
html = requests.get("https://sg.finance.yahoo.com/quote/DIS/key-statistics/", headers=headers)
# fromstring() expects a string. html.content is the string
doc = lxml.html.fromstring(html.text)

# if making a web-based API, JSON as output is better choice, easily consumed by more prog languages
# if planning to do data analysis/manipulation, CSV might be more suitable, can import into Excel

# get whole div
valuation_measures = doc.xpath('//div[@id="Col1-0-KeyStatistics-Proxy"]')[0]

# get whole table within the div
table = valuation_measures.xpath('.//table[@class="W(100%) Bdcl(c) "]')[0]

# get measure_names within the table
measure_names = table.xpath('.//span/text()')

measure_values = table.xpath('.//td[@class="Fw(500) Ta(end) Pstart(10px) Miw(60px)"]/text()')

# not yet JSON, its just a list of dictionaries
output = []
for info in zip(measure_names, measure_values):
    resp = {}
    # resp['valuation_measure'] = info[0] - giving them new names
    # resp['stats'] = info[1]
    resp[info[0]] = info[1] # using measure_name as the key and measure_value as the value
    output.append(resp)

# json_output = json.dumps(output)
# output and json_output looks the same

with open('output.json', 'w') as f:
    json.dump(output, f)
