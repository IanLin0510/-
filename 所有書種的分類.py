import requests
from bs4 import BeautifulSoup 
url = 'https://www.books.com.tw/web/books_nbtopm_01/?o=1&v=1&#39'; 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
html = requests.get(url,headers=headers).text
soup = BeautifulSoup(html,'lxml')

soupdiv = soup.find('div', class_='mod_b type02_l001-1 clearfix')
hrefs= soupdiv.select('a') 

classifyData = list()
for i in range(len(hrefs)):
    classifyData.append([ hrefs[i]['href'], hrefs[i].string])

for i in classifyData:
    print('分類編號:', i[0][-2:], '\t', i[1].string)
    print('分類網址:', i[0])
