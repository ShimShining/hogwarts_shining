# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestsuite2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_searchbaidu(self):
    self.driver.get("https://www.baidu.com/")
    time.sleep(3)
    self.driver.set_window_size(960, 724)
    self.driver.find_element(By.ID, "kw").send_keys("python")
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win1437"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["undefined"])
    self.driver.close()
    self.driver.close()
    self.driver.find_element(By.ID, "su").click()
    element = self.driver.find_element(By.ID, "su")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.close()
  
