from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from yx_project.spiders.WeChatPub import WeChatPub


KEYS = {'电动工具'}
class YX:
    def __init__(self):
        self.browser = self.share_browser()
    def share_browser(self):
        # 创建浏览器操作对象
        path = 'chromedriver.exe'
        # 打开浏览器
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser=webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
        # 访问网站
        url = "http://dzcg.ytc.com.cn"
        browser.get(url)
        # 获取网页内容
        content = browser.page_source
        # 元素定位
        a = browser.find_element(By.XPATH, '//div[@class="navbar"]//div/ul/li[3]/a')
        # 点击导航栏目中采购公告
        a.click()
        return browser
    # 监控网页数据
    def web_monitoring(self):
        #  采购公告网页监控
        li_list = self.browser.find_elements(By.XPATH, '//div[6]/div/div[2]/ul[1]/li')
        for li in li_list:
            name = li.find_element(By.TAG_NAME, 'a').text
            for k in KEYS:
                flag = k in name
                if flag:
                    # 判断企业名称是否符合关键词，发送企业微信提示用户
                    wechat = WeChatPub()
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    wechat.send_msg(f"<div class=\"gray\">{timenow}</div> <div class=\"normal\">注意！</div><div class=\"highlight\">{name}</div>")



if __name__ == "__main__":
    yx = YX()
    yx.web_monitoring()


