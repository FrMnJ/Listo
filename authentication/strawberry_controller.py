from typing import List
from models import User
from strawberry_schemas import UserType

class Queries:
    async def get_all_users(self) -> List[UserType]:
        """
        Fetch all users from the database.
        """
        users = await User.all()
        return [UserType(**user.dict()) for user in users]
    
    async def get_user_by_id(self, id: int) -> UserType:
        """
        Fetch a user by its ID from the database.
        """
        user = await User.get_or_none(id=id)
        if user:
            return UserType(**user.dict())
        return None
    
    async def get_user_by_username(self, username: str) -> UserType:
        """
        Fetch a user by its username from the database.
        """
        user = await User.get_or_none(username=username)
        if user:
            return UserType(**user.dict())
        return None
    
    async def get_user_by_email(self, email: str) -> UserType:
        """
        Fetch a user by its email from the database.
        """
        user = await User.get_or_none(email=email)
        if user:
            return UserType(**user.dict())
        return None
    
    async def get_user_by_phone(self, phone: str) -> UserType:
        """
        Fetch a user by its phone number from the database.
        """
        user = await User.get_or_none(phone_number=phone)
        if user:
            return UserType(**user.dict())
        return None