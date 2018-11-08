import requests
from bs4 import BeautifulSoup as soup
import lxml
import json

conn = requests.session()
URL = "https://manybooks.net"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
cookies = '__cfduid=db5c188ec60699c832a3c15bb8d1c05751541396763; _ga=GA1.2.860560924.1541396853; _gid=GA1.2.683960064.1541656324; _gat=1; SSESS638aad2a38a8d64c64f7efc3ac6b5c0b=xyXHUF-T5uCO_oTmlOwMEuYLezFPy2DSBH9UBKfNu3Q; __unam=6cb5566-166e2925d4d-3d6a6b94-32'
cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split(';')}

booklist = []
downlist = []
cate_dict = {
    "business":"69",
    "classic":"15",
    "history":"12",
    "science":"25",
    "travel":"42"
}
for k,v in cate_dict.items():
    for i in range(10):
        res = requests.get(url=URL + "/search-book?language=en&field_genre[%s]=%s&search=&sort_by=field_downloads&page=%s" % (v,v,i),
                           headers=headers, cookies=cookies)
        content = soup(res.content,"lxml")
        for j in content.find_all('article'):
            booklist.append(j['about'])
    print('%s列表完成' % k)
    for i in booklist:
        downdict = {}
        res = requests.get(URL+i,headers=headers, cookies=cookies)
        content = soup(res.content,"lxml")
        downdict['book_name'] = content.find('div',attrs={'itemprop':'name'}).text
        downdict['img_url'] = URL+content.find('img',attrs={'itemprop':'image'})['src']
        downdict['file_url'] = URL+content.find('a', attrs={'name': 'download'})['href']
        downdict['category'] = k
        downlist.append(downdict)

book_json = {}
book_json['data'] = downlist
print(json.dumps(book_json))


