from fastapi import FastAPI
from app.api import ingredients, categories, users

app = FastAPI()

# Routers
app.include_router(ingredients.router, prefix="/ingredients", tags=["Ingredients"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(users.router, prefix="/users", tags=["Users"])
