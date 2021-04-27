from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os,time,sys

#path=sys.path[0]+r'/browsermob-proxy-2.1.4/bin/browsermob-proxy'
#server = Server(path)
#server.start()
#proxy = server.create_proxy()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
#要访问的地址
base_url = "https://zh.cam4.com/qsx222"
#proxy.new_har("cam4", options={ 'captureContent': True})

driver.get(base_url)

#此处最好暂停几秒等待页面加载完成，不然会拿不到结果
time.sleep(60)
#result = proxy.har
print(driver.page_source)
#print(result)
#for entry in result['log']['entries']: 
#    _url = entry['request']['url']
#    # 根据URL找到数据接口,这里要找的是 http://git.liuyanlin.cn/get_ht_list 这个接口 
#    if "m3u8" in _url: 
#        print(_url) 
#        _response = entry['response'] 
#        _content = _response['content'] 
#    # 获取接口返回内容 
#        print(_response)

#server.stop()
driver.quit()
