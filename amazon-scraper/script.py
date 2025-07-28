import time
import pandas as pd
import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


logging.basicConfig(
    filename='scraper.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

query = 'iphone'

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.amazon.eg/?language=en_AE")
    time.sleep(2)

    search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'puis-card-container')]")
    results = []

    for card in cards:
        try:
            title = card.find_element(By.XPATH, ".//h2[contains(@class, 'a-size-base-plus')]//span").text
            price = card.find_element(By.XPATH, ".//span[contains(@class, 'a-price-whole')]").text
            link = card.find_element(By.XPATH, ".//a[contains(@class, 'a-link-normal') and contains(@class, 's-line-clamp-4') and contains(@class, 's-link-style') and contains(@class, 'a-text-normal')]").get_attribute('href')

            product_info = {
                'Title': title,
                'Price': price,
                'Link': link
            }

            driver.execute_script("window.open(arguments[0]);", link)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)

            try:
                stars = driver.find_element(By.XPATH, '//*[@id="acrPopover"]/span[1]/a/span')
                product_info['Stars'] = stars.text
            except Exception as e:
                logging.warning(f"Couldn't find stars for product: {e}")
                product_info['Stars'] = 'N/A'

            rows = driver.find_elements(By.XPATH, '//*[@id="poExpander"]/div[1]/div/table//tr')
            for row in rows:
                try:
                    cells = row.find_elements(By.TAG_NAME, 'td')
                    if len(cells) >= 2:
                        key = cells[0].find_element(By.TAG_NAME, 'span').text.strip()
                        value = cells[1].find_element(By.TAG_NAME, 'span').text.strip()
                        if key and value:
                            product_info[key] = value
                except Exception as e:
                    logging.warning(f"Error reading spec row: {e}")
                    continue

            results.append(product_info)

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            logging.error(f"Error parsing card: {e}")
            continue

finally:
    driver.quit()


df = pd.DataFrame(results)
df.to_excel('amazon_products.xlsx', index=False)
logging.info("Data saved to amazon_products.xlsx")
print("Scraping complete. Data saved.")
