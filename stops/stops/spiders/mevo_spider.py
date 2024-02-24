import scrapy
import json
from pydantic import BaseModel, ValidationError, validator
from ..validators import validate_fields, validate_coordinates



class Mevo(BaseModel):
    station_id: str
    address: str
    lat: float
    lon: float

    _validate_fields = validator('station_id', 'address', 'lat', 'lon')(validate_fields)
    _validate_coordinates = validator('lat', 'lon')(validate_coordinates)


class MevoSpider(scrapy.Spider):
    name = "mevo"
    start_urls = [
        'https://gbfs.urbansharing.com/rowermevo.pl/station_information.json'
    ]

    def parse(self, response):
        data = json.loads(response.body)
        for station in data['data']['stations']:
            address_parts = station['address'].split(',')
            address = address_parts[0]
            try:
                mevo_data = Mevo(station_id=station['station_id'], address=address, lat=station['lat'], lon=station['lon'])
                yield mevo_data.dict()
            except ValidationError as e:
                self.logger.error(f"Validation error: {e}")