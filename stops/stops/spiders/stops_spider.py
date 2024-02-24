#https://ckan.multimediagdansk.pl/dataset/tristar/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b
#https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json


import scrapy
import json
from pydantic import BaseModel, ValidationError, validator
from ..validators import validate_fields, validate_coordinates
from typing import Optional

class Stop(BaseModel):
    stopId: int
    stopName: Optional[str]
    stopDesc: str
    zoneName: Optional[str]
    stopLat: float
    stopLon: float

    _validate_coordinates = validator('stopLat', 'stopLon')(validate_coordinates)

class StopsSpider(scrapy.Spider):
    name = "stops"
    start_urls = ['https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json']  # Replace with the actual JSON API URL

    def parse(self, response):
        data = json.loads(response.text)

        for date, date_data in data.items():
            stops = date_data.get("stops")

            if stops:
                for stop in stops:
                    try:
                        stop_data = Stop(stopId=stop.get("stopId"), stopName=stop.get("stopName"), stopDesc=stop.get("stopDesc"), zoneName=stop.get("zoneName"), stopLat=stop.get("stopLat"), stopLon=stop.get("stopLon"))
                        yield stop_data.dict()
                    except ValidationError as e:
                        self.logger.error(f"Validation error: {e}")


# Replace 'https://example.com/api/your-json-endpoint' with the actual JSON API URL.