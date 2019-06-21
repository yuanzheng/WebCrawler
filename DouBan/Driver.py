# coding=utf-8

'''INSTALL pip install requests'''
import requests
import json
'''使用python3.6时安装好lxml时按照许多网上的教程来引入会发现etree没被引入进来 '''
# from lxml import etree
import lxml.html
from selenium import webdriver
import time

query = '王祖贤'


''' 下载图片 '''
def download(src, id):
    dir = './' + str(id) + '.webp'

    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')


def json_http_request():
    ''' for 循环 请求全部的 url, range（start，end，step=1）'''
    for i in range(0, 22, 20):
        # 从0开始下载LIMIT个数，下一次再从i+20开始
        url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start='+str(i)

        html = requests.get(url).text    # 得到返回结果
        response = json.loads(html, encoding='utf-8')   # 将 JSON 格式转换成 Python 对象
        for image in response['images']:
            print(image['src'])     # 查看当前下载的图片网址
            download(image['src'], image['id'])     # 下载一张图片


def test_range():
    for i in range(0, 22, 20):
        print("test %i" % i)


def xpath_images():

    url = 'https://movie.douban.com/subject_search?search_text=' + query + '&cat=1002'
    src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
    title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # 隐身模式打开
    driver_path = "/Users/master/projects/workspace/WebCrawler/chromedriver"
    browser = webdriver.Chrome(executable_path=driver_path, options=options)

    for i in range(0, 78, 15):
        request_url = url + '&start=' + str(i)
        print("Page %i: %s" % (i, request_url))
        browser.get(request_url)

        '''使用python3.6时安装好lxml时按照许多网上的教程来引入会发现etree没被引入进来 '''
        html = lxml.html.etree.HTML(browser.page_source)

        srcs = html.xpath(src_xpath)
        titles = html.xpath(title_xpath)
        print(srcs)

        counter = 0
        for src, title in zip(srcs, titles):
            print("Downloading %i: %s" % (counter, title.text))
            download(src, title.text)
            counter = counter + 1

        time.sleep(3)

    browser.close()



if __name__ == "__main__":

    jsonData = '{"images":[{"src": "http://google.com"},{"src": "http://facebook.com"}]}'
    input = json.loads(jsonData)

    print(input['images'][0]['src'])

    #test_range()
    xpath_images()
    # testHttpRequest()



    '''
    

    https://movie.douban.com/subject_search?search_text=%E7%8E%8B%E7%A5%96%E8%B4%A4&cat=1002
    
    var tmp = $x("//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src")
    tmp[0].nodeValue
    '''


