from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/index")
async def index(data: str,):
    return JSONResponse(
            status_code=200,
            content=data
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

