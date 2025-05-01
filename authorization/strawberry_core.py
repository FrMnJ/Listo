from typing import List, Optional 
import strawberry
from strawberry_schemas import RoleType, UserRoleDelete, UserRoleType, UserRolesOutput
from strawberry_controller import CreateMutation, DeleteMutation, Queries

@strawberry.type
class Mutation:
    create_user_role: UserRoleType = strawberry.mutation(resolver=CreateMutation.create_user_role)
    delete_user_role: UserRoleDelete = strawberry.mutation(resolver=DeleteMutation.delete_user_role)

@strawberry.type
class Query:
    roles: List[RoleType] = strawberry.field(resolver=Queries.get_all_roles)
    get_role_by_id: Optional[RoleType] = strawberry.field(resolver=Queries.get_role_by_id)
    get_role_by_name: Optional[RoleType] = strawberry.field(resolver=Queries.get_role_by_name)
    permissions: List[RoleType] = strawberry.field(resolver=Queries.get_all_permissions)
    get_permission_by_id: Optional[RoleType] = strawberry.field(resolver=Queries.get_permission_by_id)
    get_permission_by_name: Optional[RoleType] = strawberry.field(resolver=Queries.get_permission_by_name)
    get_user_roles_by_user_id: UserRolesOutput = strawberry.field(resolver=Queries.get_user_roles_by_user_id)