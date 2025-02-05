import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up ChromeDriver
chrome_driver_path = r"C:\Users\Копринков\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get("https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes?sku=white-black01-6-5-b")

# Allow time for JavaScript to load
time.sleep(5)  # Alternatively, use WebDriverWait

# Correct usage of By.CSS_SELECTOR
selector = ".titleAndAttributes--ub3i5"
elements = driver.find_elements(By.CSS_SELECTOR, selector)


for element in elements:
    print(element.text)


driver.quit()


class NikeShoesSpider(scrapy.Spider):
    name = 'nike_shoes'
    start_urls = ['https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes']

    def parse(self, response):
        product_name = response.xpath('//h1[@class=" productTitle--FWmyK"]/text()').get().strip()
        price = response.xpath('//span[@class="pricing nowPrice lg"]/text()').get().strip().replace('$', '')

        """
        Selecting dynamically-loaded content
        """

        # colour = response.xpath('//span[@class="swatchName--KWu4Q"][2]/text()').get()
        # review_count = response.xpath('//button[@class="ratingCount linkBtn focusable smallLink"]/text()').get()
        # reviews_score = response.xpath('//span[@class="ratingAvg textCaption"]/text()').get()
        # available_colours = response.xpath('//div[@class="Color-selection-name"]/text()').getall()
        # available_colours = [colour.strip() for colour in available_colours if colour.strip()]

        yield {
            'product_name': product_name,
            'price': float(price),
            # 'colour': colour,
            # 'review_count': review_count,
            # 'reviews_score': reviews_score,
            # 'availableColours': available_colours,
        }
