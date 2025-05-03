import strawberry
from typing import List, Optional

@strawberry.input 
class CarInput:
    make: str
    model: str
    year: int
    color: str
    price: float
    mileage: int
    owner_id: int

@strawberry.input
class CarUpdateInput:
    id: int
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    color: Optional[str] = None
    price: Optional[float] = None
    mileage: Optional[int] = None

@strawberry.type
class CarType:
    id: int
    make: str
    model: str
    year: int
    color: str
    price: float
    mileage: int
    owner_id: int