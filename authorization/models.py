from tortoise.models import Model
from tortoise import fields

class Role(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)

class UserRole(Model):
    id = fields.IntField(pk=True)
    user = fields.IntField() 
    role = fields.ForeignKeyField("models.Role", related_name="user_roles")

class Permission(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)

class RolePermission(Model):
    id = fields.IntField(pk=True)
    role = fields.ForeignKeyField("models.Role", related_name="role_permissions")
    permission = fields.ForeignKeyField("models.Permission", related_name="role_permissions")