from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/cars")
async def get_cars(
        page: int = 1, 
        limit: int = 10,
):
    return 
    {
        "status": "success",
        "total": 3,
        "page": 1,
        "per_page": 10,
        "total_pages": 1,
        "has_next": False,
        "has_prev": False,
        "cars" : [
            {"id": 1, "make": "Toyota", "model": "Camry", "year": 2020},
            {"id": 2, "make": "Honda", "model": "Accord", "year": 2019},
            {"id": 3, "make": "Ford", "model": "Mustang", "year": 2021},
        ]
    }

@app.get("/cars/{car_id}")
async def get_car(car_id: int):
    cars = [
        {"id": 1, "make": "Toyota", "model": "Camry", "year": 2020},
        {"id": 2, "make": "Honda", "model": "Accord", "year": 2019},
        {"id": 3, "make": "Ford", "model": "Mustang", "year": 2021},
    ]
    for car in cars:
        if car["id"] == car_id:
            return {
                "status": "success",
                "car": car
            }
    return {"error": "Car not found"}

@app.post("/cars")
async def create_car(car: dict):
    return {
            "status": "success",
            "message": "Car created",
            "car": car
           }

@app.put("/cars/{car_id}")
async def update_car(car_id: int, car: dict):
    return {
            "status": "success",
            "message": "Car updated", 
            "car_id": car_id, 
            "car": car
           }

@app.delete("/cars/{car_id}")
async def delete_car(car_id: int):
    return {
            "status": "success",
            "message": "Car deleted", 
            "car_id": car_id
           }