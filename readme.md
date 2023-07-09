# Documention of torob bot

torob has a product search engain on iranian online store. this engain have a public api resource can get from header of html file in script tags or use the api.torob.ir domain.

to this script we use the web page scrapeing and extract product information and get product more_product_url for use infomation from page.

## Solutions:
- Get categories list
    for get categories list we need to scaping on the home page of torob.com. we use javascript script for extracting this information. you can find here:
    `/utils/categories.js`

# Getting start:
run this codes for config python virtual envirement.
- `python -m venv .venv` or `python3 -m venv .venv`
- `pip install -r re.txt`
- `source ./.venv/bin/activate`

now can run scripts. ; )

### Example
here a sample example of use this script for getting default products from torob

```python
#./main.py

import json
from src.torob_craweler import TorobBot

torob_client = TorobBot()

# Get default category Products object @returned List[CategoryProductDto] data
products = torob_client.get_category_products_object()

# Get a product full information
product = torob_client.get_product(products[0])

# write product information in json file
open("data_result.json","w").write(json.dumps(product.__dict__))
```
and run this code `python ./main.py` . enjoyed.

# TorobApi class API

* ## get all products from a category.
    request to torob api and getting the list of product there is a category. if category item in pageUrl method is empty
        by default request for `175` category id.

    Args: 
    > category (CategoryDto): Category dto

    Returns:
    > List[CategoryProductDto] (optional): list of a product on the category.

    **use:**
    ```python
    ...

    products = torob_client.get_category_products_object()
    ```
* ## get product information.
    get product information from CategoryProductDto object
    
    Args: 
    > item (CategoryProductDTO): product from category

    Returns:
    > ProductDTO: product full information

    **use:**
    ```python
    ...

    products = ... # List[CategoryProductDto]
    product = torob_client.get_product(products[0])
    ```
* ## get varient of product information.
    if product have a multiply varient you need to get varient information.
    
    Args: 
    > varient (VarientItem): product selected varient

    Returns:
    > ProductDTO: product full information

    **use:**
    ```python
    ...

    products = ... # List[CategoryProductDto]
    product = torob_client.get_product(products[0])
    varient_product = torob_client.get_product_varient_information(product.variants[0].items[1]) # return ProductDto

    ```