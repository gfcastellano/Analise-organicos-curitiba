import scrapy


class SitiomaissaudeSpider(scrapy.Spider):
    name = 'sitiomaissaude'
    start_urls = [
        'https://www.sitiomaissaude.com.br/produtos/'
        ]

    def parse(self, response):
        for produto in response.xpath("//ul[@class='row list-products block list-unstyled grid']//li"):
            yield {
            'nome':  produto.xpath(".//h2/text()").get(),
            'preco': produto.xpath(".//div[@class='text-primary price']/text()").get()
            }
        
        


