import re
import csv
import pandas as pd

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
        temp = [title, str(x.contents[1].contents[1].contents[1].attrs['title']),
                str(x.contents[1].contents[1].contents[1].attrs['href']),
                str(x.contents[1].contents[5].contents[0].strip())]

        # # opening the csv file in 'a+' mode
        file = open('result.csv', 'a')
        #
        # # writing the data into the file
        with file:
            write = csv.writer(file)
            write.writerow(temp)
        # dict = {'Category': temp[0], 'Headline': temp[1], 'Link': temp[2], 'Detail': temp[3]}
        # df = pd.DataFrame(dict,index=[0])
        # saving the dataframe

        # df.to_csv('GFG.csv')
    print('\n\n\n\n')

    # titles.append(x.children)

# print(titles[0])
