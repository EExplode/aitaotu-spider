import requests
from bs4 import BeautifulSoup

url = 'http://jandan.net/ooxx'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
index = 1

def sava_jpg(res_url):
    global  index
    link_list = BeautifulSoup(requests.get(res_url, headers=headers).text, 'lxml').find_all('a', {'class': 'view_img_link'})
    for i in link_list:
        link = 'http:' + i.get('href') #图片链接
        file_name = 'C:\\Users\\only\\Desktop\\my\\' + str(index) + '.jpg'
        with open(file_name,'wb') as jpg:
            jpg.write(requests.get(link).content)
        index += 1
        print(file_name)

if __name__ == '__main__':
    for i in range(0,65):
        #页面链接
        url='http:' + BeautifulSoup(requests.get(url, headers=headers).text, 'lxml').find('a',{'class':'previous-comment-page'}).get('href')
        print('爬取第%d页...' % (65-i))
        print("链接：" + url)
        sava_jpg(url)
