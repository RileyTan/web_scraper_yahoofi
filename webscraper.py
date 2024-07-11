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
pattern = re.compile(r'/\* -- Data -- \*/[\s\S]*')
scripts = soup.find_all('script')

for script in scripts:
    if pattern.search(script.string):
        script_data = script.string
        print(script_data[:500])
        break


