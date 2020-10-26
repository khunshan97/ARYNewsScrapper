import re

import requests
from bs4 import BeautifulSoup

url = 'http://www.arynews.tv/en/'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")

match = soup.find_all('li', id=re.compile('^menu-item-.*'))
navLinks = []
for x in match:
    navLinks.append(x.next.attrs['href'])

print(navLinks)

for link in navLinks[1:11]:
    url = link

    # url = 'https://arynews.tv/en/category/pakistan/'
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, "html.parser")

    # match = soup.find_all('a', class_="post-url post-title")
    # match = soup.find_all('div', class_="item-inner clearfix")
    # match = soup.find_all('div', {'class': re.compile("item-inner clearfix$")})
    # print(match)

    try:
        title = soup.find('span', class_="h-title").contents[0]
        print(title)
    except AttributeError:
        continue
    match = soup.find_all('article')
    for x in match:
        try:
            print(x.contents[1].contents[1].contents[1].attrs['title'])
            print(x.contents[1].contents[1].contents[1].attrs['href'])
            print(x.contents[1].contents[5].contents[0].strip() + '\n')
        except AttributeError:
            continue
        except IndexError:
            continue
        except KeyError:
            continue
    print('\n\n\n\n')

    # titles.append(x.children)

# print(titles[0])
