from fastapi import FastAPI 

app  = FastAPI()

@app.get("/check")
async def check():
    power = "check"
    return {
        'status': 200,
        'data': [],
        'message': "Succesffull"
    }