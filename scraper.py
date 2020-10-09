from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')



for link in soup.find_all('a'):
    print(link.get('href'))

# for button in soup.find(class_= 'button button--primary'):
#     print(button)

# featured_header = soup.find('div', {'class': 'featured'}).h2
# print(featured_header.get_text())

# divs = soup.find('div', {'class': 'featured'})

# print(soup.div)