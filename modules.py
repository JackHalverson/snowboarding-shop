from pydantic import BaseModel
from enum import Enum


class Snowboard(BaseModel):
    id: int
    length: int
    color: str
    has_bindings: bool
    brand: str

class Brands(Enum):
    NITRO = "Nitro"
    SALOMAN = "Saloman"
    BURTON = "Burton"