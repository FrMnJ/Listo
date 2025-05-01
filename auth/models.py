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

    def dict(self) -> dict:
        """Convert the User instance to a dictionary for serialization."""
        return {
            "id": self.id,
            "username": self.username,
            "full_name": self.full_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "last_login": self.last_login,
            "is_verified": self.is_verified,
            "language": self.language,
            "utm_source": self.utm_source,
            "device_used": self.device_used,
            "location": self.location,
            "url_profile": self.url_profile,
            "url_drive_license": self.url_drive_license,
            "url_identification": self.url_identification,
            "deleted_at": self.deleted_at
        }

class Role(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

class UserRole(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user_roles")
    role = fields.ForeignKeyField("models.Role", related_name="user_roles")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

class Permission(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

class RolePermission(Model):
    id = fields.IntField(pk=True)
    role = fields.ForeignKeyField("models.Role", related_name="role_permissions")
    permission = fields.ForeignKeyField("models.Permission", related_name="role_permissions")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)