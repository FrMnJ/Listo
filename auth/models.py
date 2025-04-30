from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    full_name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    phone_number = fields.CharField(max_length=15, unique=True)
    address = fields.TextField()
    hashed_password = fields.CharField(max_length=255)
    last_login = fields.DatetimeField(null=True)
    is_verified = fields.BooleanField(default=False)
    language = fields.CharField(max_length=10, default='en')
    utm_source = fields.CharField(max_length=50, default="Other")
    device_used = fields.CharField(max_length=50, null=True)
    location = fields.CharField(max_length=100, null=True)
    url_profile = fields.CharField(max_length=255, null=True)
    url_drive_license = fields.CharField(max_length=255, null=True)
    url_identification = fields.CharField(max_length=255, null=True)
    deleted_at = fields.DatetimeField(null=True)