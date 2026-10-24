from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)


driver.get("https://the-internet.herokuapp.com/login")

print("Website:", driver.current_url)
print("Title:", driver.title)

driver.save_screenshot("headless_output.png")

print("Screenshot saved successfully!")

driver.quit()