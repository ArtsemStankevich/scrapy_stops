#https://ckan.multimediagdansk.pl/dataset/tristar/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b
#https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json


import scrapy
import json
from pydantic import BaseModel, ValidationError, validator

class Stop(BaseModel):
    stopId: int
    stopName: str
    stopDesc: str
    zoneName: str
    stopLat: float
    stopLon: float

    @validator('stopLat', 'stopLon')
    def validate_coordinates(cls, value):
        if value < -90 or value > 90:
            raise ValueError('Invalid latitude or longitude value')
        return value

class StopsSpider(scrapy.Spider):
    name = "stops"
    start_urls = ['https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json']  # Replace with the actual JSON API URL

    def parse(self, response):
        data = json.loads(response.text)

        for date, date_data in data.items():
            stops = date_data.get("stops")

            if stops:
                for stop in stops:
                    print("BBB")
                    stop_data = {
                        "stopId": stop.get("stopId"),
                        "stopName": stop.get("stopName"),
                        "stopDesc": stop.get("stopDesc"),
                        "zoneName": stop.get("zoneName"),
                        "stopLat": stop.get("stopLat"),
                        "stopLon": stop.get("stopLon"),
                    }

                    yield stop_data

# Replace 'https://example.com/api/your-json-endpoint' with the actual JSON API URL.