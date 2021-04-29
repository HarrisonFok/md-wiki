from fastapi import FastAPI, HTTPException, Response, status

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

articles = []

class Article(BaseModel):
    name: str
    content: str

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/articles/")
async def get_all():
    return articles

@app.get("/articles/{name}")
async def read_article(name: str):
    for article in articles:
        if (article.name == name):
            return article.content
    raise HTTPException(status_code=404, detail="Not Found")

@app.put("/articles/{name}", status_code=200)
async def create_article(article: Article, response: Response):
    found = False
    foundArt = None
    for art in articles:
        if (art.name == article.name):
            found = True
            foundArt = art
    if (not found):
        articles.append(article)
        response.status_code = status.HTTP_201_CREATED
    else:
        foundArt.content = article.content