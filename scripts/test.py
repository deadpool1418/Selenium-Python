from selenium import webdriver
import time

driver = webdriver.Chrome("/home/cypher/Persistent/Selenium-Python/resources/chromedriver");

driver.get("https://www.google.com");
driver.find_element_by_name("q").send_keys("wikipedia")
time.sleep(2)
driver.find_element_by_name("btnK").click()
time.sleep(2)
driver.find_element_by_link_text("Wikipedia").click()
time.sleep(2)
driver.find_element_by_name("search").send_keys("Selenium")
time.sleep(2)
driver.find_element_by_id("searchButton").click();
actualTitle = driver.title

def test_title():
    assert "Selenium" in actualTitle
driver.quit()    