import requests
from bs4 import BeautifulSoup

photo_type = 'dmtp'  # 资源类型
pages = 1  # 爬取页数
path = 'C:\\photos\\'  # 保存路径
index = 1
website = 'https://www.aitaotu.com'
headers = {'referer': 'https://www.aitaotu.com',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}


def save_jpg(url):
    url_jpg = BeautifulSoup(requests.get(url, headers=headers).text, 'lxml').find('div', {'id': 'big-pic'}).find(
        'img').get('src')
    # print('图片源地址：' + url_jpg)
    global index
    file_name = path + str(index) + '.jpg'
    with open(file_name, 'wb') as jpg:
        jpg.write(requests.get(url_jpg, headers=headers).content)
    index += 1
    print(file_name)


def paser_url_2(url):
    url_list_2 = BeautifulSoup(requests.get(url, headers=headers).text, 'lxml').find('div',
                                                                                     {'class': 'pages'}).find_all('a')
    try:
        url_list_2[0]['href'] = url.replace('https://www.aitaotu.com', '')
    except IndexError as e:
        print("此套图在同一个界面，跳过.")
    else:
        for k in url_list_2:
            url_3 = website + k.get('href')
            # print('图片链接：' + url_3)
            save_jpg(url_3)


def paser_url_1(url):
    url_list_1 = BeautifulSoup(requests.get(url, headers=headers).text, 'lxml').find('div', {
        'id': 'infinite_scroll'}).find_all('a', {'class': 'img_album_btn'})
    temp = 1
    for j in url_list_1:
        url_2 = website + j.get('href')
        print("#" * 30)
        print('爬取第' + str(temp) + '个套图：')
        temp += 1
        paser_url_2(url_2)


def main():
    url_1 = 'https://www.aitaotu.com/' + photo_type + '/'
    for i in range(0, pages):
        print('爬取第' + str(i + 1) + '个页面：')
        paser_url_1(url_1)
        url_1 = 'https://www.aitaotu.com/' + photo_type + '/list_' + str(i + 2) + '.html'


if __name__ == '__main__':
    main()
