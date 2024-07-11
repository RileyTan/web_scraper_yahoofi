import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests


url_stats = 'https://sg.finance.yahoo.com/quote/{}/key-statistics/'
url_profile = 'https://sg.finance.yahoo.com/quote/{}/profile/'
url_financials = 'https://sg.finance.yahoo.com/quote/{}/financials/'

stock = 'DIS'

response = requests.get(url_financials.format(stock))
soup = BeautifulSoup(response.text, 'lxml')

# there are many scripts, use re to solve. also, compile() lets us reuse a pattern
pattern = re.compile(r'/\* -- Data -- \*/')
script_tag = soup.find('script', text=pattern)
if script_tag is not None:
    script_data = script_tag.contents[0]
else:
    print("No match found")

#script_data = soup.find('script', text=pattern).contents[0]

#print(script_data[:500])
