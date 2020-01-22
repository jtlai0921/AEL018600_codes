from selenium import webdriver

imdb_home = "https://www.imdb.com/"
driver = webdriver.Firefox(executable_path="YOURGECKODRIVERPATH") # Use Firefox
driver.get(imdb_home)
print(driver.current_url)
driver.close()