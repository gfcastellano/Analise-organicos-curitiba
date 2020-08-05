import scrapy


class OrganicosinboxSpider(scrapy.Spider):
    name = 'organicosinbox'
    start_urls = [
        'https://www.organicosinbox.com.br/mercado'
        ]

    def parse(self, response):
        for produto in response.xpath("//div[@class='cardcestas']"):
            yield {
            'nome':  produto.xpath(".//h3/text()").get(),
            'preco': produto.xpath(".//h1/text()").get()
            }
        
        


