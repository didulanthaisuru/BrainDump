from fastapi import APIRouter, HTTPException
from schemas.user_signup import SignupRequest, SignupResponse
from services.user_signup import signup as signup_service

router = APIRouter(prefix="/signup", tags=["signup"])

@router.post("/signup", response_model=SignupResponse)
async def signup_endpoint(user_data: SignupRequest):
    user = await signup_service(user_data)
    return user

@router.get("/test-db")
async def test_database():
    from database_config import Collection_user, database, client
    try:
        # Test the connection by counting documents
        count = await Collection_user.count_documents({})
        
        # Get database info
        db_info = {
            "database_name": database.name,
            "collection_name": Collection_user.name,
            "user_count": count,
            "connection_string": str(client.address),
            "message": "Database connection successful"
        }
        
        # List all collections in the database
        collections = await database.list_collection_names()
        db_info["collections"] = collections
        
        return db_info
    except Exception as e:
        return {"error": f"Database connection failed: {str(e)}"}
