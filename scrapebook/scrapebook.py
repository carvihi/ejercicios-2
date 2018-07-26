#!/usr/bin/env python
# -*- coding: utf-8 -*-

from beautifulsoup import BeautifulSoup
from urllib2 import urlopen

url= "https://scrapebook22.appspot.com/"
response = urlopen(url).read()
soup = BeautifulSoup(response)

print soup.html.head.title.string

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        email = person_soup.find("span", attrs={"class": "email"}).string
        name = person_soup.find("div", attrs={"class": "col-md-8"}).h1.string
        city = person_soup.find("span", attrs={"data-city": True}).string
        print name + "," + email + "," + city


        csv_file = open("list.csv", "w")
        csv_file.write(name + "," + email + "," + city + "\n")

        csv_file.close()


