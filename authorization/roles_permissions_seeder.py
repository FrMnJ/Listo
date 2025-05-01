from roles_permissions import ROLES, PERMISSIONS
from models import Role, Permission, RolePermission

async def seed_roles_permissions():
    for role_name in ROLES:
        role_obj = await Role.get_or_none(name=role_name)
        if not role_obj:
            role_obj = await Role.create(name=role_name)
            print(f"Created role: {role_name}")
        else:
            print(f"Role already exists: {role_name}")

        for permission_name in PERMISSIONS[role_name]:
            permission_obj = await Permission.get_or_none(name=permission_name)
            if not permission_obj:
                permission_obj = await Permission.create(name=permission_name)
                print(f"Created permission: {permission_name}")
            else:
                print(f"Permission already exists: {permission_name}")

            role_permission_obj = await RolePermission.get_or_none(role=role_obj, permission=permission_obj)
            if not role_permission_obj:
                await RolePermission.create(role=role_obj, permission=permission_obj)
                print(f"Assigned permission '{permission_name}' to role '{role_name}'")
            else:
                print(f"Role '{role_name}' already has permission '{permission_name}'")