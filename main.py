from fastapi import FastAPI

import json

from modules import Snowboard, Brands


app = FastAPI()

with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

@app.get("/snowboarding")
async def get_boards() -> list[Snowboard]:
    return snowboard_list

@app.get("/snowboarding/{id}")
async def get_board(id: Brands) -> list[Snowboard]:
    return [board for board in snowboard_list if board["brand"] == id.value]

@app.post("/snowboarding")
async def post_board(board: Snowboard):
    snowboard_list.append(board)

@app.put("/snowboarding/{id}")
async def put_board(id: int, board: Snowboard):
    snowboard_list[id] = board

@app.delete("/snowboarding/{id}")
async def delete_board(id: int):
    snowboard_list.pop(id-1)