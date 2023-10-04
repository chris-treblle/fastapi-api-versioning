from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.v1.main import router as v1_router
from app.v2.main import router as v2_router
from config.settings import API_VERSIONS
from app.middleware.QueryParameterVersioning import QueryParameterVersioning

app = FastAPI(
    title="My FastAPI Project",
    description="A FastAPI project with versioned APIs.",
    version="1.0.0",
)

app.add_middleware(QueryParameterVersioning)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix=f"/{API_VERSIONS[0]}", tags=[API_VERSIONS[0]])
app.include_router(v2_router, prefix=f"/{API_VERSIONS[1]}", tags=[API_VERSIONS[1]])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
