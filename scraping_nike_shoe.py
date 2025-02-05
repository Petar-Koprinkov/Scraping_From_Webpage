import scrapy


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


