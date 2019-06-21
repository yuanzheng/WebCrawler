# Download Images from Web Site #

## DouBan中的项目（极客时间，数据分析实战45讲）## 
a) 下载需要下载 ChromeDriver 模拟浏览器的行为
   1. 下载ChromeDriver  http://chromedriver.storage.googleapis.com/index.html 找到与当前chrome版本对应的
   2. 别的浏览器也有对应的 Driver, https://selenium-python.readthedocs.io/installation.html

b) XPath 是 XML 的路径语言，实际上是通过元素和属性进行导航，帮我们定位位置
    ```Bash
    src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
    title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
    ```

c) 利用selenium来模拟浏览器翻页操作
    ```Bash
    from selenium import webdriver

    url = 'https://movie.douban.com/subject_search?search_text=' + query + '&cat=1002'

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # 隐身模式打开
    driver_path = "/Users/master/projects/workspace/WebCrawler/chromedriver"
    browser = webdriver.Chrome(executable_path=driver_path, options=options)
    ```
