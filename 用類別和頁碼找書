#輸入分類跟頁面
import requests
from bs4 import BeautifulSoup
b=0
number=0
cat=int(input('請輸入分類編號'))
pag=int(input('請輸入頁碼'))
page=[]
c=[]
for i in hrefs:
    c.append(i['href'])
url='https://www.books.com.tw/web/books_nbtopm_01/?o=1&v=1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
html = requests.get(url,headers=headers).text
soup = BeautifulSoup(html,'lxml')
soupdiv1 = soup.find('div', class_='page')
p=soupdiv1.find_all('a')
url = 'https://www.books.com.tw/web/books_nbtopm_'+'{}'.format(c[cat][42:44])+'/?o=1&v=1&page='+str(pag)
for i in range(1,2):
    page.append('https://www.books.com.tw/web/books_nbtopm_'+'{}'.format(c[cat][42:44])+'/?o=1&v=1&page'+'{}'.format(pag))
for i in range(1,2):
    url=page[b]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    html = requests.get(url,headers=headers).text
    soupPageURL = BeautifulSoup(html,'lxml')
    soupPageURLdiv = soupPageURL.find_all('div',{'class':'mod type02_m012 clearfix'})
    soupPageURLDivItem= soupPageURLdiv[0].select('.item')
    b=b+1
    for item in soupPageURLDivItem:
        msg = item.select('.msg')[0] 
        src = item.select('img')[1]['src']
        title = msg.select('a')[0].text        
        imgurl = src.split("?i=")[-1].split("&")[0]  
        author = msg.select('a')[1].text       
        publish = msg.select('a')[2].text       
        date = msg.find('span').text.split("：")[-1] 
        onsale = item.select('.price .set2')[0].text 
        content = item.select('.txt_cont')[0].text.replace(" ","").strip()  
        number+=1
        print("第", number, "本書")
        print("書名：" + title)   
        print("圖片網址：" + imgurl)  
        print("作者：" + author)      
        print("出版社：" + publish)  
        print("出版日期：" + date) 
        print(onsale)                   
        print("內容：" + content)
        print()
