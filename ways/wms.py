#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BasePage import Page
import time

class wmsPage(Page):
    loginName_loc = (By.ID, 'loginName')
    loginPassword_loc = (By.ID, 'password')
    clickLogin_loc = (By.ID, 'loginBtn')
    title_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div')
    prompt_loc = (By.CSS_SELECTOR, '.text')
    clickLoginName_loc = (By.CSS_SELECTOR, ".dropdown-toggle")
    clickQuit_loc = (By.CSS_SELECTOR, '.md-trigger')
    clickConfirm_loc = (By.CSS_SELECTOR, '.btn.btn-danger.md-close')

    def typeUsername(self, username):
        self.wait
        self.find_element(*self.loginName_loc).send_keys(username)  # 输入登录名

    def typePassword(self, password):
        self.wait
        self.find_element(*self.loginPassword_loc).send_keys(password)  # 输入密码

    def loginButton(self):
        self.wait
        self.find_element(*self.clickLogin_loc).click()  # 点击登录按钮
        # time.sleep(5)

    def login(self, username, password):
        self.typeUsername(username)
        self.typePassword(password)
        self.loginButton()
        self.wait
        self.find_element(*self.clickLogin_loc).send_keys(Keys.ENTER)

    def get_title(self):  #获取页面title
        self.wait
        return self.find_element(*self.title_loc).text

    def get_prompt(self):  #获取提示信息
        self.wait
        return self.find_element(*self.prompt_loc).text

    def exitLogin(self):  #退出登录
        self.wait
        self.find_element(*self.clickLoginName_loc).click()
        self.wait
        self.find_element(*self.clickQuit_loc).click()
        self.wait
        self.find_element(*self.clickConfirm_loc).click()


