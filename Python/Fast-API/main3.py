#making just a Hello WOrld API

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "This is a simple API created using FASTAPI by me (Soubhik Sadhu);"}