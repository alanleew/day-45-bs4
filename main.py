import requests
import pprint as pp
from bs4 import BeautifulSoup
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage,"html.parser")
# print(soup.prettify())

# soup.find_all(name="a") # Searching by name of tag
# soup.find(name="h1", id="name") # Finds the first element
# soup.find(name="h3", class_="heading") # Instead of id, you can use class selector
# tag.get() allows you to get a value in a tag

# Narrowing down particular elements
# company_url = soup.select_one(selector="p a #idSelector .classSelector")

titlelines = soup.select(".titleline > a")
titlelines_list = [i.getText() for i in titlelines]
# pp.pprint(titlelines_list)

urls = soup.select(".sitestr")
urls_list = [i.getText() for i in urls]
# print(len(urls_list))
# pp.pprint(urls_list)

upvotes = soup.select(".score")
upvotes_list = [int(i.getText().split()[0]) for i in upvotes]
# print(upvotes_list)

upvotes_max = max(upvotes_list)
max_index = upvotes_list.index(upvotes_max)

print(titlelines_list[max_index])
print(urls_list[max_index])
print(str(upvotes_list[max_index])+" upvotes")

# TODO: Note about ethics of webscraping, use robots.txt after endpoint to see what the website allows for webscraping
# https://news.ycombinator.com/robots.txt
