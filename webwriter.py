from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from typing import Optional, List
from utils import getFile
from utils import remove_accents
from bs4 import BeautifulSoup as bs
import pickle as pickle
from pathlib import Path


HERE = Path(__file__).parent
URL = "http://laptrinhonline.club"
BASE_URL = "http://laptrinhonline.club/problems/?hide_solved=1&page="
LOGIN_URL = "http://laptrinhonline.club/accounts/login/?next="
COOKIES_FILE = HERE / "cookies.pickle"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
EXEC_PATH = "chromedriver"

def program_exit():
    print("Đã đạt giới hạn, đang thoát...")
    exit()

class Automator:
    def __init__(
            self,
            cookies_file: str = COOKIES_FILE,
            login: Optional[str] = None,
            driver_path: str = EXEC_PATH,
            max: Optional[int] = 510,
            password: Optional[str] = None,
            sleep: Optional[int] = 2,):

        self.cookies_file = cookies_file
        self.max = max
        self.login = login
        self.password = password
        self.driver_path = driver_path
        self.browser = None
        self.sleep = sleep

    def init_browser(self, headless: Optional[bool] = False) -> None:
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--disable-popup-blocking")
        options.add_argument(f"user-agent={USER_AGENT}")

        self.browser = webdriver.Chrome(
            options=options,
        )

        if not headless:
            self.__auth()
        self.__set_cookies()

    def __set_cookies(self) -> None:
        self.browser.get(LOGIN_URL)
        with open(self.cookies_file, "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                if "expiry" in cookie:
                    cookie["expiry"] = int(cookie["expiry"])
                    self.browser.add_cookie(cookie)

    def __init_headless_browser(self) -> None:
        """
        Recreating browser in headless mode(without GUI)
        """
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-popup-blocking")
        options.add_argument(f"user-agent={USER_AGENT}")
        self.browser = webdriver.Chrome(
            options=options,
        )

    def __auth(self) -> None:
        """
        Đăng nhập lần đầu để save cookies
        """
        self.browser.get(LOGIN_URL)
        if not (self.login is None and self.password is None):
            self.browser.find_element(By.ID, "id_username").send_keys(self.login)
            self.browser.find_element(By.ID, "id_password").send_keys(self.password)
            self.browser.find("button").click()

        ready = input("Nhấn enter để tiếp tục sau khi đăng nhập xong...")
        with open(self.cookies_file, "wb") as f:
            pickle.dump(self.browser.get_cookies(), f)

            self.browser.close()
            # Recreating browser in headless mode for next work
            self.__init_headless_browser()

    def __set_cookies(self) -> None:
        self.browser.get(LOGIN_URL)
        with open(self.cookies_file, "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                if "expiry" in cookie:
                    cookie["expiry"] = int(cookie["expiry"])
                    self.browser.add_cookie(cookie)

    def submit(self) -> list:
        """Lặp qua từng trang của web laptrinhonline để check trùng tên với dapan
            Bất cứ file trùng nào đều sẽ được submit code"""
        count = 1
        files = getFile("./dapan")
        print(f"GIÁ TRỊ SLEEP HIỆN TẠI: {self.sleep}")
        print(f"GIÁ TRỊ MAX HIỆN TẠI: {self.max}")
        for i in range(1,21):
            self.browser.get(BASE_URL + str(i))
            soup = bs(self.browser.page_source, "html.parser")
            values = soup.find_all("td", class_="problem")

            #Lặp qua toàn bộ câu hỏi và đối chiếu đáp án
            for value in values:
                probName = remove_accents(value.text.replace("\n", ""))
                for file in files:
                    if remove_accents(file) == probName:
                        a_tags = value.find("a")
                        print(f'Đang xử lý problems ID:{a_tags["href"]} ({count})')
                        id = a_tags["href"]
                        self.browser.get(URL + id + "/submit")
                        code = open(f"./dapan/{file}.txt", "r")
                        code = code.read()
                        count += 1
                        #Xử lý alert
                        try:
                            self.browser.find_element(By.CSS_SELECTOR, "#ace_source > div > textarea").send_keys(code)
                            self.browser.find_element(By.CLASS_NAME, "button").click()
                            time.sleep(self.sleep)

                            #Xử lý trường hợp web hiện alert
                            try:
                                alert = self.browser.switch_to.alert
                                alert.accept()
                                continue
                            except:
                                print(f"Hoàn thành {probName}")

                        #Bỏ qua các bài lỗi:
                        except Exception as e:
                            print(f"Gặp lỗi tại {probName}: {e}")
                            continue
                        if count == self.max:
                            program_exit()
