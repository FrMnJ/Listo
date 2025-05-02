from typing import List
from models import Role, Permission, UserRole
from strawberry_schemas import RoleType, PermissionType, RoleWithUserRoleIdType, UserRoleDelete, UserRoleInput, UserRoleType, UserRolesOutput, UserType
from inter_service_communication import get_user

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
        for permission in permissions:
            await permission.fetch_related("roles")
        return [PermissionType(
                                id=permission.id, 
                                name=permission.name,
                            ) for permission in permissions]
    async def get_permission_by_id(self, id: int) -> PermissionType:
        """
        Fetch a permission by its ID from the database.
        """
        permission = await Permission.get_or_none(id=id)
        if permission:
            await permission.fetch_related("roles")
            return PermissionType(id=permission.id, name=permission.name)
        return None
    
    async def get_permission_by_name(self, name: str) -> PermissionType:
        """
        Fetch a permission by its name from the database.
        """
        permission = await Permission.get_or_none(name=name)
        if permission:
            await permission.fetch_related("roles")
            return PermissionType(id=permission.id, name=permission.name)
        return None
    
    async def get_user_roles_by_user_id(self, user_id: int) -> UserRolesOutput:
        """
        Fetch all roles for a user by its ID from the database.
        """
        user = await get_user(user_id)
        if not user:
            raise ValueError("User not found")

        user_roles = await UserRole.filter(user=user["id"]).prefetch_related("role")
        roles = [
                  {
                    "id": user_role.id,
                    "role": user_role.role
                  } for user_role in user_roles]
        for role in roles:
            await role["role"].fetch_related("permissions")
        roles = [
            RoleWithUserRoleIdType(
                    id=role["role"].id, 
                    user_role_id=role["id"],
                    name=role["role"].name, 
                     permissions=[
                         PermissionType(id=permission.id, name=permission.name)
                         for permission in role["role"].permissions
                     ]) for role in roles
        ]
        return UserRolesOutput(user_id=user["id"], roles=roles)
    
class CreateMutation:
    async def create_user_role(self, user_role_input: UserRoleInput) -> UserRoleType:
        """
        Create a new user role in the database.
        """
        user = await get_user(user_role_input.user_id)
        if not user:
            raise ValueError("User not found")

        role = await Role.get_or_none(name=user_role_input.role) 
        await role.fetch_related("permissions")
        if not role:
            raise ValueError("Role not found")

        user_role = await UserRole.create(
            user = user["id"],
            role = role,
        )
        return UserRoleType(
                            id=user_role.id, 
                            user=user["id"], 
                            role=RoleType(
                                id=role.id, 
                                name=role.name, 
                                permissions=[
                                    PermissionType(id=permission.id, name=permission.name)
                                    for permission in role.permissions
                                ]
                            )
                        )
class DeleteMutation:
    async def delete_user_role(self, user_role_id: int) -> UserRoleDelete:
        """
        Delete a user role from the database.
        """
        user_role = await UserRole.get_or_none(id=user_role_id).fetch_related("role")
        if not user_role:
            raise ValueError("User role not found")
        
        await user_role.delete()
        return UserRoleDelete(
            id=user_role.id, 
            user_id=user_role.user, 
            role_id=user_role.role.id
        )