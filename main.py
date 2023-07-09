import json
from src.torob_craweler import TorobBot

torob_client = TorobBot()

# Get default category Products object @returned List[CategoryProductDto] data
products = torob_client.get_category_products_object()

# Get a product full information
product = torob_client.get_product(products[0])
varient_product = torob_client.get_product_varient_information(product.variants[0].items[1])

# write product information in json file
open("data_result.json","w").write(json.dumps(product.__dict__))