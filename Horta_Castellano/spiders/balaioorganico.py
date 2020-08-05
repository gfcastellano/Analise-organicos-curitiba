import scrapy


class BalaioorganicoSpider(scrapy.Spider):
    name = 'balaioorganico'
    start_urls = [
        'https://www.balaioorganico.com.br/categoria-produto/frutas/',
        'https://www.balaioorganico.com.br/categoria-produto/legumes-e-verduras/',
        'https://www.balaioorganico.com.br/categoria-produto/legumes-e-verduras/page/2/'
        ]

    def parse(self, response):
        for produto in response.xpath("//div[@class='product-details']"):
            yield {
            'nome':  produto.xpath(".//h3//a/text()").get(),
            'preco': produto.xpath(".//span[@class='price']//span[@class='woocommerce-Price-amount amount']/text()").get()
            }
        
        


