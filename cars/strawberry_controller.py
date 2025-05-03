from typing import List
from models import Car
from strawberry_schemas import CarType, CarInput, CarUpdateInput
from inter_service_communication import check_authorization, AuthorizationOuput
from strawberry.types import Info

class Queries: 
    async def get_all_cars(self) -> List[CarType]:
        """
        Fetch all cars from the database.
        """
        cars = await Car.all()
        return [CarType(id=car.id, 
                        make=car.make, 
                        model=car.model, 
                        year=car.year, 
                        color=car.color,
                        price=car.price,
                        mileage=car.mileage,
                        owner_id=car.owner_id,) for car in cars]
    async def get_car_by_id(self, id: int) -> CarType:
        """
        Fetch a car by its ID from the database.
        """
        car = await Car.get(id=id)
        if car:
            return CarType(id=car.id, 
                           make=car.make, 
                           model=car.model, 
                           year=car.year, 
                           color=car.color,
                           price=car.price,
                           mileage=car.mileage,
                           owner_id=car.owner_id,)
        return None
    async def get_cars_by_user_id(self, user_id: int) -> List[CarType]:
        """
        Fetch all cars owned by a specific user.
        """
        cars = await Car.filter(owner_id=user_id)
        return [CarType(id=car.id, 
                        make=car.make, 
                        model=car.model, 
                        year=car.year, 
                        color=car.color,
                        price=car.price,
                        mileage=car.mileage,
                        owner_id=car.owner_id,) for car in cars]
    
    async def get_cars_by_model(self, model: str) -> List[CarType]:
        """
        Fetch all cars of a specific model.
        """
        cars = await Car.filter(model=model)
        return [CarType(id=car.id, 
                        make=car.make, 
                        model=car.model, 
                        year=car.year, 
                        color=car.color,
                        price=car.price,
                        mileage=car.mileage,
                        owner_id=car.owner_id,) for car in cars]
    
    async def get_cars_by_make(self, make: str) -> List[CarType]:
        """
        Fetch all cars of a specific brand.
        """
        cars = await Car.filter(make=make)
        return [CarType(id=car.id, 
                        make=car.make, 
                        model=car.model, 
                        year=car.year, 
                        color=car.color,
                        price=car.price,
                        mileage=car.mileage,
                        owner_id=car.owner_id,) for car in cars]
    async def get_cars_by_year(self, year: int) -> List[CarType]:
        """
        Fetch all cars of a specific year.
        """
        cars = await Car.filter(year=year)
        return [CarType(id=car.id, 
                        make=car.make, 
                        model=car.model, 
                        year=car.year, 
                        color=car.color,
                        price=car.price,
                        mileage=car.mileage,
                        owner_id=car.owner_id,) for car in cars]
    async def get_cars_by_color(self, color: str) -> List[CarType]: 
        """
        Fetch all cars of a specific color.
        """
        cars = await Car.filter(color=color)
        return [CarType(id=car.id, 
                        make=car.make, 
                        model=car.model, 
                        year=car.year, 
                        color=car.color,
                        price=car.price,
                        mileage=car.mileage,
                        owner_id=car.owner_id,) for car in cars]
    async def get_cars_by_price(self, price: float) -> List[CarType]:
        """
        Fetch all cars within a specific price range.
        """
        cars = await Car.filter(price__lte=price)
        return [CarType(id=car.id, 
                        make=car.make, 
                        model=car.model, 
                        year=car.year, 
                        color=car.color,
                        price=car.price,
                        mileage=car.mileage,
                        owner_id=car.owner_id,) for car in cars]
    async def get_cars_by_mileage(self, mileage: int) -> List[CarType]:
        """
        Fetch all cars within a specific mileage range.
        """
        cars = await Car.filter(mileage__lte=mileage)
        return [CarType(id=car.id, 
                        make=car.make, 
                        model=car.model, 
                        year=car.year, 
                        color=car.color,
                        price=car.price,
                        mileage=car.mileage,
                        owner_id=car.owner_id,) for car in cars]

class CreateMutation: 
    async def create_car(self, car_input: CarInput, info: Info) -> CarType:
        """
        Create a new car in the database.
        """
        # Extract the request from the context
        request = info.context["request"]
        
        # Get the token from the Authorization header
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            raise Exception("Invalid or missing token")
        token = token.split(" ")[1]

        authorize = await check_authorization(token, action="create", object="car")
        user = authorize.User
        if not user:
            raise Exception("User not found")
        car_input.owner_id = user["id"]
        car = await Car.create(**car_input.__dict__)
        return CarType(id=car.id, 
                       make=car.make, 
                       model=car.model, 
                       year=car.year, 
                       color=car.color,
                       price=car.price,
                       mileage=car.mileage,
                       owner_id=user["id"],)

class UpdateMutation:
    async def update_car(self, car_input: CarUpdateInput, info: Info) -> CarType:
        """
        Update an existing car in the database.
        """
        # Extract the request from the context
        request = info.context["request"]
        
        # Get the token from the Authorization header
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            raise Exception("Invalid or missing token")
        token = token.split(" ")[1]

        authorize = await check_authorization(token, action="update", object="car")
        user = authorize.User
        if not user:
            raise Exception("User not found")
        car = await Car.get(id=car_input.id)
        if not car:
            raise Exception("Car not found")
        if car.owner_id != user["id"]:
            raise Exception("User not authorized to update this car")
        for key, value in car_input.__dict__.items():
            if value is not None:
                setattr(car, key, value)
        await car.save()
        return CarType(id=car.id, 
                       make=car.make, 
                       model=car.model, 
                       year=car.year, 
                       color=car.color,
                       price=car.price,
                       mileage=car.mileage,
                       owner_id=user["id"],)

class DeleteMutation:
    async def delete_car(self, id: int, info: Info) -> bool:
        """
        Delete a car from the database.
        """
        # Extract the request from the context
        request = info.context["request"]
        
        # Get the token from the Authorization header
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            raise Exception("Invalid or missing token")
        token = token.split(" ")[1]

        authorize = await check_authorization(token, action="remove", object="car")
        user = authorize.User
        if not user:
            raise Exception("User not found")
        car = await Car.get(id=id)
        if not car:
            raise Exception("Car not found")
        if car.owner_id != user["id"]:
            raise Exception("User not authorized to delete this car")
        await car.delete()
        return True