from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

#브라우저 꺼짐 방지 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager(version="114.0.5735.90").install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
browser.get("https://www.ted.com/talks/young_ha_kim_be_an_artist_right_now/transcript?language=ko")

# script list 받아오기
script_list = browser.find_elements(By.CSS_SELECTOR, "#maincontent > div.w-full.px-5.md\:px-10.xl\:px-16.bg-white > div > div > aside > div.pt-6.lg\:pl-8.lg\:pr-2.xl\:pl-12.xl\:pr-4.css-1fh91ol.exa0j0u1 > div.open.css-1b8n8c1.exa0j0u4 > div > div > div.mx-auto.mb-10.w-full > div > div > span > span")

for i in range(0,len(script_list)):
    print(i+1)
    print(script_list[i].text)