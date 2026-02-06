# Name: selenium-test.py
# Date: 03 Feb 2026
# Description: un script para intentar hacer web scraping de storygraph CON SELENIUM

# import the required library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
# instantiate a Chrome options object
options = webdriver.ChromeOptions()

# set the options to use Chrome in headless mode
options.add_argument("--headless=new")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
 
# initialize an instance of the Chrome driver (browser) in headless mode
driver = webdriver.Chrome(options=options)

# visit your target site
# driver.get("https://www.scrapingcourse.com/ecommerce/")
url = "https://thestorygraph.com/"

try:
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    print(driver.page_source)  # Print the page source
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

# # GET 1
# product_data = {
#     "Url": driver.find_element(
#         By.CSS_SELECTOR, ".woocommerce-LoopProduct-link"
#     ).get_attribute("href"),
#     "Image": driver.find_element(By.CSS_SELECTOR, ".product-image").get_attribute(
#         "src"
#     ),
#     "Name": driver.find_element(By.CSS_SELECTOR, ".product-name").text,
#     "Price": driver.find_element(By.CSS_SELECTOR, ".price").text,
# }
# print(product_data)

# # GET 2
# products = driver.find_elements(By.CSS_SELECTOR, ".product")
# for product in products:

#     # extract the elements into a dictionary using the CSS selector
#     product_data = {
#         "Url": product.find_element(
#             By.CSS_SELECTOR, ".woocommerce-LoopProduct-link"
#         ).get_attribute("href"),
#         "Image": product.find_element(By.CSS_SELECTOR, ".product-image").get_attribute(
#             "src"
#         ),
#         "Name": product.find_element(By.CSS_SELECTOR, ".product-name").text,
#         "Price": product.find_element(By.CSS_SELECTOR, ".price").text,
#     }
# print(product_data)

# output the full-page HTML
print(driver.page_source)

# release the resources allocated by Selenium and shut down the browser
driver.quit()
