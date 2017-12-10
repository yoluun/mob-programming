
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.willflyforfood.net/2017/03/31/the-ultimate-japanese-food-guide-what-to-eat-in-japan-and-where-to-try-them/")

soup = BeautifulSoup(page.content, 'html.parser')

repr(soup)