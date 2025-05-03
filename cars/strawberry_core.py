from typing import List
from strawberry_controller import CreateMutation, DeleteMutation, Queries, UpdateMutation
import strawberry 
from strawberry_schemas import CarInput, CarType

@strawberry.type
class Query: 
    cars: List[CarType] = strawberry.field(resolver=Queries.get_all_cars)
    get_car_by_id: CarType = strawberry.field(resolver=Queries.get_car_by_id)
    get_cars_by_user_id: List[CarType] = strawberry.field(resolver=Queries.get_cars_by_user_id)
    get_cars_by_model: List[CarType] = strawberry.field(resolver=Queries.get_cars_by_model)
    get_cars_by_make: List[CarType] = strawberry.field(resolver=Queries.get_cars_by_make)
    get_cars_by_year: List[CarType] = strawberry.field(resolver=Queries.get_cars_by_year)
    get_cars_by_color: List[CarType] = strawberry.field(resolver=Queries.get_cars_by_color)
    get_cars_by_price: List[CarType] = strawberry.field(resolver=Queries.get_cars_by_price)
    get_cars_by_mileage: List[CarType] = strawberry.field(resolver=Queries.get_cars_by_mileage)

@strawberry.type
class Mutation:
    create_car: CarType = strawberry.mutation(resolver=CreateMutation.create_car)
    update_car: CarType = strawberry.mutation(resolver=UpdateMutation.update_car)
    delete_car: bool = strawberry.mutation(resolver=DeleteMutation.delete_car)