import constants
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import dotenv_values
from LinkedinParser import LinkedinParser


class LinkedinScraper:
    def __init__(self, profile_images_filepath):
        self.config = dotenv_values(".env")
        self.profile_images_filepath = profile_images_filepath
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def login_to_linkedin(self):
        self.driver.get(constants.LOGIN_PAGE)
        time.sleep(constants.WAIT_TIME_LOAD)
        self.driver.find_element(By.ID, "username").send_keys(self.config["USER"])
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(self.config["PASSWORD"])
        password_input.send_keys(Keys.ENTER)

    def scroll_to_botom(self):
        start = time.time()
        initialScroll = 0
        finalScroll = 1000
        while True:
            self.driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
            initialScroll = finalScroll
            finalScroll += 1000
            time.sleep(constants.WAIT_TIME_LOAD)
            end = time.time()
            if round(end - start) > (constants.WAIT_TIME_LOAD*5):
                break

    def process_recommendations(self):
        self.driver.get(constants.RECOMMENDATIONS_URL)
        self.scroll_to_botom()
        self.src_recommendations_page = self.driver.page_source

    def scrape_recommendations(self, url):
        self.login_to_linkedin()
        self.process_recommendations()

        lp = LinkedinParser(self.src_recommendations_page)
        lp.process_recommendations()

        self.driver.quit()

