import scrapy
import json

class MevoSpider(scrapy.Spider):
    name = "mevo"
    start_urls = [
        'https://gbfs.urbansharing.com/rowermevo.pl/station_information.json'
    ]
    '''
    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }
    '''
    def parse(self, response):
        data = json.loads(response.body)
        for station in data['data']['stations']:
            address_parts = station['address'].split(',')
            address = address_parts[0]
            yield {
                'id':int(station['station_id']), 
                'address':address, 
                'lat':station['lat'], 
                'lon':station['lon']
            }
