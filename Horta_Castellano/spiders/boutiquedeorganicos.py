import scrapy


class BoutiquedeorganicosSpider(scrapy.Spider):
    name = 'boutiquedeorganicos'
    #allowed_domains = ['https://boutiquedeorganicos.com.br/legumes.html']
    start_urls = [
        'https://boutiquedeorganicos.com.br/legumes.html',
        'https://boutiquedeorganicos.com.br/legumes.html?p=2',
        'https://boutiquedeorganicos.com.br/legumes.html?p=3',
        'https://boutiquedeorganicos.com.br/legumes.html?p=4',
        'https://boutiquedeorganicos.com.br/folhas.html',
        'https://boutiquedeorganicos.com.br/folhas.html?p=2',
        'https://boutiquedeorganicos.com.br/frutas.html',
        'https://boutiquedeorganicos.com.br/frutas.html?p=2',
        'https://boutiquedeorganicos.com.br/frutas.html?p=3'
        ]

    def parse(self, response):
        for produto in response.xpath("//div[@class='product-info']"):
            yield {
            'nome':  produto.xpath(".//h2//a/text()").get(),
            'preco': produto.xpath(".//span[@class='price']/text()").get(),
            'unidade': produto.xpath(".//span[@class='marca-label']/text()").get()
            }
        
        


