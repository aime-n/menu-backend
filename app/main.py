from fastapi import FastAPI
from app.api import ingredients, categories
from app.database import init_db

app = FastAPI()

# Initialize the database
init_db()  

# Routers
app.include_router(ingredients.router, prefix="/ingredients", tags=["Ingredients"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
