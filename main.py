from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.shared.infraestructure.api import router as shared_router
from src.mountains.infraestructure.api import router as mountain_router
from src.mountains.domain.exception import MountainImgNotValid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(MountainImgNotValid)
def mountain_img_not_valid_handler(request: Request, exc: MountainImgNotValid) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={"detail": "The provided image URL is not valid."},
    )


app.include_router(shared_router)
app.include_router(mountain_router)



