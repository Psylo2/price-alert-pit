from pydantic import BaseModel, validator
from typing import Dict


class StoreModel(BaseModel):
    store_id: str
    name: str
    url_prefix: str
    tag_name: str
    query: Dict

    @validator('store_id', 'name', 'url_prefix', 'tag_name')
    def validate_string(cls, str_):
        if not isinstance(str_, type(str)):
            raise TypeError("type must be string")
        return str_

    @validator('query')
    def validate_dict(cls, dict_):
        if not isinstance(dict_, type(Dict)):
            raise TypeError("type must be dict")
        return dict_

