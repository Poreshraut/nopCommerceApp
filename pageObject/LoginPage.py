from selenium.webdriver.common.by import By


class LoginPage:
    txt_username = "//input[@id='Email']"
    txt_password = "//input[@id='Password']"
    btn_login = "//button[@type='submit']"
    btn_logout = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.txt_username).clear()
        self.driver.find_element(By.XPATH, self.txt_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_password).clear()
        self.driver.find_element(By.XPATH, self.txt_password).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.btn_login).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH, self.btn_logout).click()
