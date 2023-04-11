from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from constants import globalConstants as gc

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(gc.URL)

    # def wait_for_element(self, locator, timeout=5):
    #     return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    def test_invalid_login(self):
        # element = self.wait_for_element((By.ID, "user-name"), timeout=5)
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userId = self.driver.find_element(By.NAME,"user-name")
        userId.send_keys("1")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passId = self.driver.find_element(By.NAME,"password")
        passId.send_keys("1")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        logBut = self.driver.find_element(By.NAME,"login-button")
        logBut.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        errorMsg = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        ErrorText = errorMsg.text
        if ErrorText == gc.ERROR_TEXT:
            print("Test Başarili")
        # sleep(15)
    def test_valid_login(self):
        self.driver.get(gc.URL)
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))

        

        userId = self.driver.find_element(By.NAME,"user-name")
        # userId.send_keys("standard_user")

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        

        passId = self.driver.find_element(By.NAME,"password")
        # passId.send_keys("secret_sauce")
        
        #action chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userId,"standard_user")
        actions.send_keys_to_element(passId,"secret_sauce")
        actions.perform()

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))

        logBut = self.driver.find_element(By.NAME,"login-button")
        logBut.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        
        
        
        
        
        

testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()

# while True:
#     continue