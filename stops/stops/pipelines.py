from itemadapter import ItemAdapter
from .validators.main_validators import validate_text_fields, validate_coordinates, validate_id, validate_address

class StopsPipeline:
    def process_item(self, item, spider):
        return item

class ValidationPipelineStops:
    def process_item(self, item, spider):
        if spider.name == 'stops':
            try:
                item['id'] = validate_id(item['id'])
                item['stopName'] = validate_text_fields(item['stopName'])
                item['stopDesc'] = validate_text_fields(item['stopDesc'])
                item['zoneName'] = validate_text_fields(item['zoneName'])
                item['lat'] = validate_coordinates(item['lat'])
                item['lon'] = validate_coordinates(item['lon'])
                item['url'] = spider.start_urls[0]
            except ValueError as e:
                print(f"Validation error: {e}")
                print(item['url'])
                raise DropItem(f"Validation error: {e}")
            return item
        else:
            return item

class ValidationPipelineMevo:
    def process_item(self, item, spider):
        if spider.name == 'mevo':
            try:
                item['id'] = validate_id(item['id'])
                item['address'] = validate_address(item['address'])
                item['lat'] = validate_coordinates(item['lat'])
                item['lon'] = validate_coordinates(item['lon'])
                item['url'] = spider.start_urls[0]
            except ValueError as e:
                print(f"Validation error: {e}")
                print(item['url'])
                raise DropItem(f"Validation error: {e}")
            return item
        else:
            return item
