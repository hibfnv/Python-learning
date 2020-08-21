from urllib.request import Request, urlopen
import re
import ssl
# 去除ssl数据签名影响系统的问题
ssl._create_default_https_context = ssl._create_unverified_context


# r has a set error
def get_page(url):
    r = Request(url, headers={
        # 模拟浏览器
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
                                                                                         })
    resp = urlopen(r)
    return resp.read().decode("utf-8")


def parse_page(s):
    obj = re.compile(r'<div class="item">.*?<em class="">(?P<Num>.*?)</em>.*?<span'
                     r' class="title">(?P<movie>.*?)</span>.*?<span class="rating_num"'
                     r' property="v:average">(?P<rating_num>.*?)</span>.*?<spa'
                     r'n>(?P<person_num>.*?)人评价</span>', re.S)
    res = obj.finditer(s)
    lst = []
    for item in res:
        dic = item.groupdict()
        lst.append(dic)
    return lst


def main():
    f = open("douban.txt", mode='w', encoding='utf-8')
    for i in range(10):
        s = get_page(f'https://movie.douban.com/top250?start={i * 25}&filter=')
        result = parse_page(s)
        for d in result:
            f.write(str(d))
            f.write("\n")


main()
