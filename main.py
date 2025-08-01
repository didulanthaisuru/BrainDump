from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_signup import router as signup_router

app = FastAPI(
    title="BrainDump API",
    description="just dump your brain",
    version="1.0.0"
)

app.include_router(signup_router)