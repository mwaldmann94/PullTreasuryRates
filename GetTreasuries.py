import sys
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup

filename = "Treasury.csv"
f = open(filename, "w")
header = "date, 1MO, 2MO, 3MO, 6MO, 1YR, 2YR, 3YR, 5YR, 7YR, 10YR, 20YR, 30YR\n"
f.write(header)

myUrl = "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/TextView.aspx?data=yieldYear&year=2019"
#opens webpage connection
my_client = urlopen(myUrl)
#saves html from webpage
html_data = my_client.read()
#close webpage connection
my_client.close()

soup_data = Soup(html_data,"html.parser")
rate_data = soup_data.findAll("td",{"class":"text_view_data"})

count = 0
for data in rate_data:
    Post = data.string
    count += 1
    f.write(Post + ",")
    if count % 13 == 0:
        f.write("\n")


