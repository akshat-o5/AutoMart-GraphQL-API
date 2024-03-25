from typing import Optional
import strawberry

@strawberry.type
class VehicalInfo:
    id : int
    model : str
    brand : str
    type : str
    yearsOfUsage : int
    price : int
    color : str
    engineType : Optional[str]
    fuelType : Optional[str]
