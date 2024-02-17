from selenium import webdriver
import time
# Chrome 드라이버 경로 설정 (다운로드한 드라이버 경로로 설정해주세요)
chrome_driver_path = "chromedriver.exe"

# Chrome 옵션 설정 (헤드리스 모드로 실행)
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 드라이버 생성
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# 웹페이지 열기 (원하는 페이지 URL로 변경해주세요)
driver.get("https://example.com")

while True:
    time.sleep(5000000000)