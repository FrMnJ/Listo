from typing import List
from models import Role, Permission
from strawberry_schemas import RoleType, PermissionType


class Queries:
    async def get_all_roles(self) -> List[RoleType]:
        """
        Fetch all roles from the database.
        """
        roles = await Role.all()
        for role in roles:
            await role.fetch_related("permissions")
        return [RoleType(id=role.id, 
                         name=role.name, 
                         permissions=[
                             PermissionType(id=permission.id, name=permission.name)
                             for permission in role.permissions
                         ]) for role in roles]

    async def get_role_by_id(self, id: int) -> RoleType:
        """
        Fetch a role by its ID from the database.
        """
        role = await Role.get_or_none(id=id)
        if role:
            await role.fetch_related("permissions")
            return RoleType(id=role.id, 
                            name=role.name, 
                            permissions=[
                                PermissionType(id=permission.id, name=permission.name)
                                for permission in role.permissions
                            ])
        return None
    
    async def get_role_by_name(self, name: str) -> RoleType:
        """
        Fetch a role by its name from the database.
        """
        role = await Role.get_or_none(name=name)
        if role:
            await role.fetch_related("permissions")
            return RoleType(id=role.id, 
                            name=role.name, 
                            permissions=[
                                PermissionType(id=permission.id, name=permission.name)
                                for permission in role.permissions
                            ])
        return None
    
    async def get_all_permissions(self) -> List[PermissionType]:
        """
        Fetch all permissions from the database.
        """
        permissions = await Permission.all()
        return [PermissionType(id=permission.id, name=permission.name) for permission in permissions]