from fastapi import FastAPI

app=FastAPI()

food_items={
    'indian': ["Samosa","Dosa"],
    'american': ["Apple Pie", "Burger"],
    'italian' : ["Pizza", "Spegatti"]
}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    return food_items.get(cuisine)