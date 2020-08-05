import scrapy


class CestadeliverySpider(scrapy.Spider):
    name = 'cestadelivery'
    start_urls = [
        'https://www.cestasdeliveryorganico.com.br/categoria-produto/frutas/',
        'https://www.cestasdeliveryorganico.com.br/categoria-produto/legumes-tuberculos-e-raizes/',
        'https://www.cestasdeliveryorganico.com.br/categoria-produto/legumes-tuberculos-e-raizes/page/2/',
        'https://www.cestasdeliveryorganico.com.br/categoria-produto/verduras-e-folhas/',
        'https://www.cestasdeliveryorganico.com.br/categoria-produto/verduras-e-folhas/page/2/'
        ]

    def parse(self, response):
        for produto in zip(response.xpath("//ul[@class='products columns-4']//h2"),response.xpath("//ul[@class='products columns-4']//span[@class='woocommerce-Price-amount amount']")):
            yield {
            'nome':  produto[0].xpath("./text()").get(),
            'preco': produto[1].xpath("./text()").get()
            }
        
        


