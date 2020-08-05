import scrapy


class NaturezapuraSpider(scrapy.Spider):
    name = 'naturezapura'
    start_urls = [
        'https://naturezapuraorganicos.com/categoria-produto/horta/',
        'https://naturezapuraorganicos.com/categoria-produto/pomar/'
        ]

    def parse(self, response):
        for produto in response.xpath("//ul[@class='products customify-grid-5_md-5_sm-3_xs-1 wc-grid-view']//li"):
            yield {
            'nome':  produto.xpath(".//h2//a/text()").get(),
            'preco': produto.xpath(".//span[@class='woocommerce-Price-amount amount']/text()").get()
            }
        
                
        


