
##说明：运行这个项目 需要安装 selenium pyquery  模块，安装命令是pip install selenium
## 需要谷歌浏览器和安装对应版本谷歌驱动 chromedriver ,第九关课程会详细教如何安装哦
## 不会安装可以等学完课程第9关，课程有详细讲解安装
##希望大家先好好学习前面的爬虫课程，打好基础哦




from selenium import webdriver   #导入selenium第三方包的网页驱动
from selenium.common.exceptions import TimeoutException #导入selenium里的exceptions设置时间
from selenium.webdriver.common.by import By ##这个是设置查找方式的By.ID,By.CSS_SELECTOR
from selenium.webdriver.support import expected_conditions as EC  #这个是标注状态的
from selenium.webdriver.support.wait import WebDriverWait #这个是等待页面加载某些元素
from pyquery import PyQuery as pq  #PyQuery库也是一个非常强大又灵活的网页解析库，PyQuery 是 Python 仿照 jQuery 的严格实现。语法与 jQuery 几乎完全相同，所以不用再去费心去记一些奇怪的方法了。

from urllib.parse import quote #句法分析，可见它的作用就是用来解析传进来的URL地址，并输出相应的信息

# browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 10)  #创建浏览器对象



def index_page(page,a):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')

    try:

        url = 'https://s.taobao.com/search?q=' + quote(a)  #拼接爬取地址
        browser.get(url)   #访问网址
        if page > 1:   #默认是第一页 所以如果页码大于1
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))  #页面元素判断等待处理。
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))  ##页面元素判断等待处理。
            input.clear()           #清空之前缓存
            input.send_keys(page)   #给输入框输入页码实现翻页
            submit.click()           #点击翻页
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))) #判断前端css上，“页码”按钮这个元素中存在文本：
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()  #get_products()里面利用pyquery分析网页，抓取网页元素
    except TimeoutException:   #超时
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = browser.page_source  #获得页面源码
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),   #找到css属性为.pic .img的替换属性
            'price': item.find('.price').text(),   #找到.price属性标签的文本值
            'deal': item.find('.deal-cnt').text(), #找到'.deal-cnt属性标签的文本值
            'title': item.find('.title').text(), #找到.title属性标签的文本值
            'shop': item.find('.shop').text(),   #找到.shop属性标签的文本值
            'location': item.find('.location').text()   #找到.location 属性标签的文本值
        }

        print(product)





def main():
    """
    遍历每一页
    """
    a = input("请输入要搜索的商品")
    for i in range(1, 100 + 1):
        index_page(i,a)
    browser.close()


if __name__ == '__main__':
    main()