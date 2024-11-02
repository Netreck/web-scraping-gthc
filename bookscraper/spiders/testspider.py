import scrapy
from bookscraper.items import PDF_Item

class TestspiderSpider(scrapy.Spider):
    name = "testspider"
    allowed_domains = ["prograd.ufabc.edu.br"]
    start_urls = ["https://prograd.ufabc.edu.br/sisu"]

    def parse(self, response):
        # Itera sobre cada tag <p> que contém um link <a>
        for p in response.css('p'):
            p_hrefs = p.css('a::attr(href)').getall()
            # Se houver links, adiciona-os e o conteúdo do <p> ao item
            if p_hrefs:
                for href in p_hrefs:
                    pdf_saved = PDF_Item()
                    pdf_saved['url'] = href  # Armazena cada href individualmente
                    pdf_saved['paragraph'] = p.css('::text').getall()  # Armazena o texto do <p> correspondente
                    yield pdf_saved
