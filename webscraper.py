import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests

url_stats = "https://sg.finance.yahoo.com/quote/DIS/key-statistics/"
url_profile = "https://sg.finance.yahoo.com/quote/DIS/profile/"
url_financials = "https://sg.finance.yahoo.com/quote/DIS/financials/"


