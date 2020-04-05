import scrapy


class PostsSpider(scrapy.Spider):
    name = "products"
    start_urls = [
        # 'https://www.webstaurantstore.com/10259/ice-buckets.html?vendor=American-Metalcraft',
        # 'https://www.webstaurantstore.com/3087/food-storage-containers.html?vendor=Cambro'
        'https://www.webstaurantstore.com/51003/knives.html'
    ]

    def parse(self, response):
        # find the product listing div
        product_listing = response.xpath('//*[@id="product_listing"]')
        # for each product extract data
        for product in product_listing.xpath('//*[@class="ag-item gtm-product "]'):
            yield {
                'brand': product.attrib['data-brand'],
                'category': product.attrib['data-list'],
                'description': product.attrib['data-description'],
                'price': product.attrib['data-price'],
                'vendor_item_number': product.attrib['data-item-number'][3:],
                'websta_item_number': product.attrib['data-item-number'],
                'url': product.xpath('.//div[1]/a[2]').attrib['href']
            }

        # look for the next page button, get url
        next_page = response.css('a[rel="next"]::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)