from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
app = FastAPI()
@app.get("/")
async def index(request: Request):
    return "Welcome to Golab REST API"

@app.get("/data")
async def get_data(request: Request):
    idea = request.query_params.get('idea')
    if idea:
        data = {'idea': idea}
        return JSONResponse(content=data)
    else:
        return "Please provide an idea parameter in the URL."
