import strawberry
from  typing import List, Optional
from strawberry_schemas import UserType
from strawberry_controller import Queries

@strawberry.type
class Query:
    users: List[UserType] = strawberry.field(resolver=Queries.get_all_users)
    get_user_by_id: Optional[UserType] = strawberry.field(resolver=Queries.get_user_by_id)
    get_user_by_username: Optional[UserType] = strawberry.field(resolver=Queries.get_user_by_username)
    get_user_by_email: Optional[UserType] = strawberry.field(resolver=Queries.get_user_by_email)
    get_user_by_phone: Optional[UserType] = strawberry.field(resolver=Queries.get_user_by_phone)
    
