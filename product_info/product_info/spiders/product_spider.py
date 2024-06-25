import scrapy
import re
import json

class ProductSpiderSpider(scrapy.Spider):
    name = "product_spider"
    allowed_domains = ["example.com"]
    start_urls = ['https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html']

    def parse(self, response):


        script_tag = response.css('script[type="application/ld+json"]')
        json_data = 0
        if len(script_tag) > 1:
            script_content = script_tag[1].xpath('./text()').get()

            if script_content:
                json_data = json.loads(script_content)
        
        print(json_data['AggregateRating']['ratingValue'])

        default_color = ''
        element_with_data_defaultcolor = response.css('[data-defaultcolor]')

        for elem in element_with_data_defaultcolor:
            default_color = elem.attrib['data-defaultcolor']

        sizes = []
        options = response.css('select#plp-select option')

        for option in options:
            data_attr_value = option.attrib.get('data-attr-value')

            if data_attr_value:
                sizes.append(data_attr_value)


        review_count = self.extract_numeric_value(json_data["AggregateRating"]['reviewCount'])
        review_rating = self.extract_numeric_value(json_data["AggregateRating"]['ratingValue'])
        yield {
            'name': json_data['name'],
            'price': json_data['offers']['price'],
            'color': default_color,
            'size': sizes,
            'reviews_count' : review_count,
            'review_rating' : review_rating
        }
    
        
    def extract_numeric_value(self, text):
        numeric_value = re.findall(r'\d+\.\d+|\d+', text)
        if numeric_value:
            return float(numeric_value[0])
        else:
            return None
        

