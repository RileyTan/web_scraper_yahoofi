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
