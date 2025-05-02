from typing import Tuple
import httpx

async def get_user(id: int) -> dict | None:
    """
    Fetch a user by its ID from the database from the authentication service.
    """
    query = """
    query GetUserById($id: Int!) {
        getUserById(id: $id) {
            id
            username
            fullName
            email
            phoneNumber
            location
            lastLogin
            address
            language
            utmSource
            deviceUsed
            urlProfile
            urlDriveLicense
            urlIdentification
            isVerified
            deletedAt
        }
    }
    """
    variables = {"id": id}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://authentication-service:8000/graphql",
            json={"query": query, "variables": variables},
        )
        if response.status_code == 200:
            return response.json().get("data", {}).get("getUserById")
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

async def verify_token(token: str) -> Tuple[bool, dict | None]:
        """
        Verify the token from the authentication service.
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://authentication-service:8000/verify-token",
                json={"token": token},
            )
            if response.status_code == 200:
                return (response.json().get("isValid", False),
                        response.json().get("user", {}))
            else:
                print(f"Error: {response.status_code}, {response.text}")
                return (False, None)