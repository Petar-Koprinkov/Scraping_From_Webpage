import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = r"C:\Users\Копринков\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes?sku=white-black01-6-5-b")
driver.implicitly_wait(60)


selector = ".titleAndAttributes--ub3i5"
elements = WebDriverWait(driver, 60).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
)


for element in elements:
    print(element.text)


driver.quit()

# class NikeShoesSpider(scrapy.Spider):
#     name = 'nike_shoes'
#     start_urls = ['https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes']
#     def parse(self, response):
#         product_name = response.xpath('//h1[@class=" productTitle--FWmyK"]/text()').get().strip()
#         price = response.xpath('//span[@class="pricing nowPrice lg"]/text()').get().strip().replace('$', '')
#         """
#         Selecting dynamically-loaded content
#         """
#         # colour = response.xpath('//span[@class="swatchName--KWu4Q"][2]/text()').get()
#         # review_count = response.xpath('//button[@class="ratingCount linkBtn focusable smallLink"]/text()').get()
#         # reviews_score = response.xpath('//span[@class="ratingAvg textCaption"]/text()').get()
#         # available_colours = response.xpath('//div[@class="Color-selection-name"]/text()').getall()
#         # available_colours = [colour.strip() for colour in available_colours if colour.strip()]
#         yield {
#             'product_name': product_name,
#             'price': float(price),
#             # 'colour': colour,
#             # 'review_count': review_count,
#             # 'reviews_score': reviews_score,
#             # 'availableColours': available_colours,
#         }
