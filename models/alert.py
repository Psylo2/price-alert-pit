from pydantic import BaseModel, validator


class AlertModel(BaseModel):
    alert_id: str
    name: str
    item_id: str
    price_limit: float
    user_email: str

    @validator('alert_id', 'name', 'item_id', 'user_email')
    def validate_string(cls, str_):
        if not isinstance(str_, type(str)):
            raise TypeError("type must be string")
        return str

    @validator('price_limit')
    def validate_float(cls, float_):
        if not isinstance(float_, type(float)):
            raise TypeError("type must be float")
        return float_

