from pydantic import BaseModel, validator
from typing import Dict, Optional


class ItemModel(BaseModel):
    item_id: str
    url: str
    tag_name: str
    query: Dict
    price: Optional[float]

    @validator('item_id', 'url', 'tag_name')
    def validate_string(cls, str_):
        if not isinstance(str_, type(str)):
            raise TypeError("type must be string")
        return str_

    @validator('price')
    def validate_float(cls, float_):
        if not float_:
            return float_
        if not isinstance(float_, type(float)):
            raise TypeError("type must be float")
        return float_

    @validator('query')
    def validate_dict(cls, dict_):
        if not isinstance(dict_, type(Dict)):
            raise TypeError("type must be dict")
        return dict_

