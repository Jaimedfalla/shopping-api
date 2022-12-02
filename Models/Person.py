from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class HairColor(Enum):
    WHITE="white"
    BROWN = "brown",
    BLACK="black"
    BLONDE= "blonde"
    RED = "red"

#Field is to validate each property of models
class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example ="Jaime"
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Falla",
        )
    age: int = Field(
        ...,
        gt = 0,
        le = 150,
        example=38
        )
    hair_color: Optional[HairColor] = Field(
        default=None,
        example="black",
        )
    is_married: Optional[bool] = Field(
        default=None,
        example="True",
        )

    """class Config: # This class its pourpose is generate a default values in openapi app
        schema_extra = {
            "example":{# name example is important
                "first_name": "Jaime",
                "last_name": "Falla",
                "age": 38,
                "hair_color": "black",
                "is_married": True
            }
        }"""