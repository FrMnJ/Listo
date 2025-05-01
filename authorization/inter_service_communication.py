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
