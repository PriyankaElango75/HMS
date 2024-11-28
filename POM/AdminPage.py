from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from Libary.BaseFile import BaseClass


class AdminLoginPage:
    __txt_username =("xpath","//input[@class='form-control']")
    __txt_password = ("xpath","//input[@class='form-control password']")
    __btn_login = ("xpath","//button[@class='btn btn-primary pull-right']")

    def __init__(self,driver):
        self.driver = driver

    def admin_login(self,username,password):
        b = BaseClass(self.driver)
        b.enter_text(AdminLoginPage.__txt_username,username)
        b.enter_text(AdminLoginPage.__txt_password,password)
        b.click_element(AdminLoginPage.__btn_login)
        sleep(5)





