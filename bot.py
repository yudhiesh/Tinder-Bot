from selenium import webdriver
from time import sleep
#from classified import id, password

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        # switch to login window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

       
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('')

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('')

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        sleep(2)

        # switch to base window 
        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()


    def like(self):
        like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like.click()

    def dislike(self):
        dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike.click()
    
    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = Bot()
bot.login()






