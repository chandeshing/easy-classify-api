from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


@app.get("/square")
async def calculate_square(number: float = Query(..., description="The number to square")):
    result = number ** 2
    return {"number": number, "square": result}