# 获取网易云音乐的歌单的名称和id
# 这样可以后续下载所有歌单的歌
# 哈哈哈
import requests
from bs4 import BeautifulSoup

head = {
    'Cookie': 'JSESSIONID-WYYY=EZvnB%2FGx1lxyYYpEFkInTfDAQKMrI23E0EP%2F37G7'
              'q7kIjCha6VvpkhIY8f%2B2q5rSvPPhEwvxu%2FtxR50Szq3bXcta%2F1lC%5'
              'C5EZ9or6fV6TPn9Y6p%5C5%2B60eGlru1SZ2Afp7J1rY4vBTuRjV9Blx%2Bd'
              'AO7SQw4qzE4U9BRNx7SNr%2BJwq6tZDV%3A1541000234496; _iuqxldmz'
              'r_=32; _ntes_nnid=f1813c7102d3a1c932957cc89b3b85cf,15408240'
              '57661; _ntes_nuid=f1813c7102d3a1c932957cc89b3b85cf; __utma=9'
              '4650624.652102838.1540824059.1540906385.1540908652.3; __utm'
              'z=94650624.1540906385.2.2.utmcsr=baidu|utmccn=(organic)|utm'
              'cmd=organic; WM_NI=oZwtQ0VAnVibQmp3Q9Z8BLwKK%2BihryBO88oe6q'
              'egNHS%2F0CpTEkbZyXBDJHMP8z29fdbf7tHU0OvulqSYWP%2FBIvAa1jN%2'
              'BE%2BPVGCO5%2Fzu6yqZV9EFQk3jTJZaYT6paQm8qYWY%3D; WM_NIKE=9c'
              'a17ae2e6ffcda170e2e6eebab65ebc968aa7f450b8b08fb2c44e878f8ea'
              'bb841898c96d4e76886aa81acd42af0fea7c3b92aad86b995d43c969fa2'
              'b7ec6a93b3c0d4d4339ae88eadf64189f5a789f1738291f8d9ee6ff6afa'
              'b88cd4491f100a4f36087b5aebbfc54829c86a9d05cfca6fedae570a2ba'
              'f995cb5ff491ba96ef7b918799b1ae4a8baa8f82b4628ef58bccd35e859'
              'd81d6ae72b7eab792d95efb9b8ab2ea39aa8c86bbe45398eac082d467fc'
              'af97b8dc37e2a3; WM_TID=FIGfA%2FDa7jxBQEVFBRd4PLBQcSdzA6'
              'L7; __utmb=94650624.26.10.1540998435; __utmc=94650624',
    'Host': 'music.163.com',
    'Referer': 'https://music.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'

}
url = 'https://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset=35'


def urllist():
    urllis = []
    for i in range(37):
        urllis.append('https://music.163.com/discover/playlis'
                      't/?order=hot&cat=全部&limit=35&offset={}'.format(i*35))
    return urllis


def get_each_dict(link):
    htm = requests.get(link, headers=head)
    htm.encoding = 'utf-8'
    # print(htm.text)
    htms = BeautifulSoup(htm.text, 'html.parser')
    # 找到歌单列表的标签
    gedanlist = htms.find_all('ul', class_="m-cvrlst f-cb")[0].find_all('li')
    nameidict = {}
    for each in range(35):

        # 添加到名字id字典里
        nameidict[gedanlist[each].div.a.get('title')] = \
            str(gedanlist[each].div.a.get('href')).split('=')[-1]

    return nameidict


def main():
    allid = {}
    listurl = urllist()
    for every in listurl:
        idict = get_each_dict(every)
        for i in list(idict.keys()):
            allid[i] = idict[i]
    print(len(allid))


if __name__ == '__main__':
    main()
