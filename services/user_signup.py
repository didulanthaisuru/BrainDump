from fastapi import HTTPException
from database_config import Collection_user
from schemas.user_signup import SignupRequest, SignupResponse

async def signup(user_data: SignupRequest):
    # Check if user already exists
    existing_user = await Collection_user.find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    
    # Create new user document
    user_doc = {
        "email": user_data.email,
        "password": user_data.password,  # In production, hash this password
        "name": user_data.name
    }
    
    # Insert user into database
    print(f"Attempting to insert user into collection: {Collection_user.name}")
    result = await Collection_user.insert_one(user_doc)
    print(f"User inserted with ID: {result.inserted_id}")
    print(f"User data: {user_doc}")
    
    # Verify the insertion by finding the document
    inserted_user = await Collection_user.find_one({"_id": result.inserted_id})
    print(f"Verification - Found user: {inserted_user is not None}")
    
    # Return user data without password
    return SignupResponse(
        email=user_data.email,
        name=user_data.name
    )
