from dataclasses import dataclass
from typing import List


@dataclass
class ImageDTO:
    src: str


@dataclass
class MetaDataDTO:
    key: str
    value: bool


@dataclass
class AttributeDTO:
    name: str
    slug: str
    visible: bool
    options: List[str]


@dataclass
class VarientItem:
    name1: str
    name2: str
    title: str
    price: int
    image_url: str
    slug_name: str
    shop_text: str
    selected: bool
    price_text: str
    discount_info: any
    random_key: str
    image_count: int
    show_image: bool
    stock_status: str
    more_info_url: str
    price_text_mode: str
    delivery_city_name: str
    delivery_city_flag: str
    web_client_absolute_url: str

@dataclass
class VarientDto:

    
    title: str
    items: List[VarientItem]


@dataclass
class ProductDTO:
    id: str
    name: str
    type: str
    status: str
    min_price: int
    max_price: int
    description: str
    regular_price: str
    short_description: str
    buy_box_price_text: str
    images: List[ImageDTO]
    variants: List[VarientDto]
    meta_data: List[MetaDataDTO]
    attributes: List[AttributeDTO]
