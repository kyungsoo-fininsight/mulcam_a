import scrapy
from naver_crawler.items import NaverCrawlerItem


class NaverSpider(scrapy.Spider):
    name = "naver"

    def start_requests(self):
        urls = [
            "https://search.naver.com/search.naver?query=%EA%B8%88%EB%A6%AC&where=news&ie=utf8&sm=nws_hty"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_list)

    def parse_list(self, response):
        url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=001&aid=0011841162"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = NaverCrawlerItem()
        item["url"] = response.url
        item["content"] = response.xpath(
            "//div[@id='articleBodyContents']//text()"
        ).getall()
        item["media"] = response.xpath("//div[@class='press_logo']/a/img/@alt").get()

        yield item
