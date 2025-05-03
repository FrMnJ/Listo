from tortoise.models import Model
from tortoise import fields

class Car(Model):
    id = fields.IntField(pk=True)
    make = fields.CharField(max_length=50)
    model = fields.CharField(max_length=50)
    year = fields.IntField()
    color = fields.CharField(max_length=20)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    mileage = fields.IntField()
    owner_id = fields.IntField(null=True) 

    def dict(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "price": str(self.price),
        }

