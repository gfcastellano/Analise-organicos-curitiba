import scrapy


class OhmarketSpider(scrapy.Spider):
    name = 'ohmarket'
    start_urls = [
        'https://www.ohmarket.com.br/categoria-produto/nossa-horta/',
        'https://www.ohmarket.com.br/categoria-produto/nossa-horta/page/2/',
        'https://www.ohmarket.com.br/categoria-produto/nosso-pomar/'
        ]

    def parse(self, response):
        for produto in response.xpath("//div[@class='product-details']"):
            yield {
            'nome':  produto.xpath(".//h3//a/text()").get(),
            'preco': produto.xpath(".//span[@class='price']//span[@class='woocommerce-Price-amount amount']/text()").get()
            }
        
        


