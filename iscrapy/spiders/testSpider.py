import scrapy


# 测试
class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        self.logger.info(response.status)
        pass
