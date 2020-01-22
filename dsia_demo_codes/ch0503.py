from selenium import webdriver

imdb_home = "https://www.imdb.com/"
driver = webdriver.Chrome(executable_path="YOURCHROMEDRIVERPATH") # Use Chrome
driver.get(imdb_home)
print(driver.current_url)
driver.close()