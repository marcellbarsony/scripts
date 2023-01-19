#!/usr/bin/env python3

# Dependencies: bs4, lxml

import bs4
import requests

result = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

# Scrape Content
soup = bs4.BeautifulSoup(result.text, "lxml")

# Content
#print(soup)

# Title
#print(soup.select('title')[0].getText())

# Image
valtozo = soup.select('img')
for item in soup.select('img'):
    #print(type(item))
    image_url = item['src']
    print(image_url)
    print(type(image_url))

if __name__ == '__main__':
    main()
