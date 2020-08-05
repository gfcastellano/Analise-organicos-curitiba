import scrapy


class CasadoverdureiroSpider(scrapy.Spider):
    name = 'casadoverdureiro'
    start_urls = [
        'https://www.casadoverdureiro.com.br/categoria-produto/frutas/',
        'https://www.casadoverdureiro.com.br/categoria-produto/legumes/',
        'https://www.casadoverdureiro.com.br/categoria-produto/verduras/'
        ]

    def parse(self, response):
        for produto in response.xpath("//div[@class='woocommerce columns-4']//div[@class='alus-products']"):
            yield {
            'nome':  produto.xpath(".//h3/a/text()").get(),
            'preco': produto.xpath(".//span[@class='woocommerce-Price-amount amount']/text()")[-1].get()
            }
        
        next_page = response.xpath("//li//a[@class='next page-numbers']/@href").get()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
        
        


