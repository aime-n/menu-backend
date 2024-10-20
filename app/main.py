from fastapi import FastAPI
from app.api import ingredients, categories, users, recipes

app = FastAPI()

# Routers
app.include_router(ingredients.router, prefix="/ingredients", tags=["Ingredients"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(recipes.router, prefix="/recipes", tags=["Recipes"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe Management API"}