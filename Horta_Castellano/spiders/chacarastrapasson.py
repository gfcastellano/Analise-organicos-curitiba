import scrapy


class ChacarastrapassonSpider(scrapy.Spider):
    name = 'chacarastrapasson'
    start_urls = [
        'https://chacarastrapasson.com.br/loja/'
        ]

    def parse(self, response):
        for produto in response.xpath("//ul[@class='products columns-3']//li"):
            yield {
            'nome':  produto.xpath(".//h2/text()").get(),
            'preco': produto.xpath(".//span[@class='woocommerce-Price-amount amount']/text()")[-1].get()
            }
        
        next_page = response.xpath("//li//a[@class='next page-numbers']/@href").get()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
        
        


