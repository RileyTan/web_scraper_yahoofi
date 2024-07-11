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

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
response = requests.get(url_financials.format(stock) , headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

# there are many scripts, use re to solve. also, compile() lets us reuse a pattern
pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]

#print(script_data[:500])
#print(script_data[-500:])

# searching deeper
start = script_data.find("context")-2
json_data = json.loads(script_data[start:-12])
json_data['context'].keys
