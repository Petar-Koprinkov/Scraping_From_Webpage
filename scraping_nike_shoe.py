import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

chrome_driver_path = r"C:\Users\Копринков\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes?sku=white-black01-6-5-b")
driver.implicitly_wait(60)

selector = ".wrapper--VuqBA:nth-child(1) .focusable , .productTitle--FWmyK , .lg , .textCaption , #pdpContentWrapper .smallLink , .horizontalBorder--Npbxe .swatchName--KWu4Q"
elements = WebDriverWait(driver, 100).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
)

result = [element.text.strip() for element in elements if element.text.strip()]
print(result)
final_result = {
    'name': result[0],
    'price': result[1],
    'colour': result[4],
    "reviews_count": int(result[3].strip("()")),
    "reviews_score": float(result[2]),
}

with open("product_details.json", "w", encoding="utf-8") as json_file:
    json.dump(final_result, json_file, ensure_ascii=False, indent=4)

print(final_result)

driver.quit()
