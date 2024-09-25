from fastapi import FastAPI
import json
from modules import Snowboard, Brands

app = FastAPI()

with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

@app.get("/snowboarding")
async def get_boards() -> list:
    return snowboard_list

@app.get("/snowboarding/{id}")
async def get_board(id: Brands) -> list:
    return [board for board in snowboard_list if board["brand"] == id.value]

@app.post("/snowboarding")
async def post_board(board: Snowboard):
    snowboard_list.append(board.model_dump())

@app.put("/snowboarding/{id}")
async def put_board(id: int, board: Snowboard):
    for idx, item in enumerate(snowboard_list):
        if item['id'] == id:
            snowboard_list[idx] = board.model_dump()
            return {"message": "Snowboard updated successfully"}

    snowboard_list.append(board.model_dump())
    return {"message": "Snowboard created successfully"}

@app.delete("/snowboarding/{id}")
async def delete_board(id: int):
    for idx, item in enumerate(snowboard_list):
        if item['id'] == id:
            snowboard_list.pop(idx)
            return {"message": "Snowboard deleted successfully"}

    return {"error": "Snowboard not found"}
