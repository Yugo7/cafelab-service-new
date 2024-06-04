from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import router

app = FastAPI(
    title="COFFELAB",
    description="API for integration with COFFELAB",
    version="1.0.00",
    docs_url="/coffelab-api-swagger",
    redoc_url="/coffelab-api-docs",
    servers=[
        {
            "url": "https://coffelab-api.onrender.com/",
            "description": "Production",
        },
        {
            "url": "http://127.0.0.1:8000/",
            "description": "Local server",
        }

    ]
)


@app.get("/")
async def read_root():
    return "Welcome to coffelab´s API!, to check docs type /coffelab-api-swagger in the url"


app.include_router(router.user_router.router, prefix="/user", tags=["user"])
app.include_router(router.admin_router.router, prefix="/admin", tags=["admin"])
app.include_router(router.contact_router.router, prefix="/contact", tags=["contact"])
app.include_router(router.newsletter_router.router, prefix="/newsletter", tags=["newsletter"])
app.include_router(router.image_router.router, prefix="/upload", tags=["upload"])
app.include_router(router.product_router.router, prefix="/product", tags=["product"])
app.include_router(router.payments_router.router, prefix="/payments", tags=["payments"])
app.include_router(router.events_router.router, prefix="/events", tags=["events"])
app.include_router(router.orders_router.router, prefix="/orders", tags=["orders"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

