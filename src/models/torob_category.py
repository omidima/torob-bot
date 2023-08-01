from dataclasses import dataclass
from typing import Union

@dataclass
class CategoryProductDTO:
    category_id: Union[str,None] = None
    image_url: Union[str,None] = None
    discount_info: Union[list,None] = None
    random_key: Union[str,None] = None
    name1: Union[str,None] = None
    name2: Union[str,None] = None
    more_info_url: Union[str,None] = None
    web_client_absolute_url: Union[str,None] = None
    price: Union[int,None] = None
    price_text: Union[str,None] = None
    price_text_mode: Union[str,None] = None
    shop_text: Union[str,None] = None
    stock_status: Union[str,None] = None
    delivery_city_name: Union[str,None] = None
    delivery_city_flag: Union[str,None] = None
    image_count: Union[int,None] = None

@dataclass
class CategoryDto:
    name: str
    id: int