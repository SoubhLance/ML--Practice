from fastapi import FastAPI
import enum

app=FastAPI()

food_items={
    'indian': ["Samosa","Dosa"],
    'american': ["Apple Pie", "Burger"],
    'italian' : ["Pizza", "Spegatti"]
}

class Available_Cuisines(str,enum.Enum):
    indian= "indian"
    american = "american"
    italian = "italian"


@app.get("/get_items/{cuisine}")
async def get_items(cuisine: Available_Cuisines):
    return food_items.get(cuisine)