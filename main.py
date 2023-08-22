from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

data = []
# keep pages <= 200/
pages = 50

for page in range(1,pages+1):
    driver.get(f"https://www.prioritytire.com/shop/?p={page}#/perpage:100")
    tyres = 100
    for tyre in range(1,tyres+1):
        tyre_details = {}

        tyre_card = driver.find_element(By.XPATH,f"//*[@id='searchspring-content']/div[2]/div/div/ul/li[{tyre}]/article")
        price = tyre_card.find_element(By.CSS_SELECTOR,'span.price.price--withoutTax.ng-binding').text
        full_name = tyre_card.find_element(By.CSS_SELECTOR,'h4.card-title').text
        name = tyre_card.find_element(By.CSS_SELECTOR,'p.card-text.ng-binding').text
        details = tyre_card.find_element(By.CSS_SELECTOR,'span.product-sku.ng-binding').text
        
        tyre_details["NAME"] = name
        tyre_details["FULL_NAME"] = full_name
        tyre_details["PRICE"] = price
        tyre_details["DETAILS"] = details
        data.append(tyre_details)

# print(len(data))
df = pd.DataFrame(data)
df.to_csv(f"Output_of_{pages}_pages.csv", index=False)
print("CSV file created successfully.")