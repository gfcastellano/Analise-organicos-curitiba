import scrapy


class Chacara3corregosSpider(scrapy.Spider):
    name = 'chacara3corregos'
    start_urls = [
        'https://www.chacara3corregos.com.br/sub/Frutas-verduras-legumes-e-temperos/5ee23ad66ecb63969f798a64?page=1',
        'https://www.chacara3corregos.com.br/sub/Frutas-verduras-legumes-e-temperos/5ee23ad66ecb63969f798a64?page=2'
        ]

    def parse(self, response):
        for produto in response.xpath("//div[@class='ib-products-grid']//div//single-item"):
            yield {
            'nome':  produto.xpath(".//span[@class='ib-single-item-info-name']/text()").get(),
            'preco': produto.xpath(".//span[@class='ib-single-item-info-price']/text()").get()
            }
        
        #next_page = response.xpath("//li//a[@class='next page-numbers']/@href").get()
        #if next_page is not None:
        #    next_page_link = response.urljoin(next_page)
        #    yield scrapy.Request(url=next_page_link, callback=self.parse)
        
        


