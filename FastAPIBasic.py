from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the data model for the article input
class ArticleInput(BaseModel):
    name: str

# Variable to store the most recently posted article name
latest_article_name = None

# Define the POST endpoint to accept an article name
@app.post("/articles")
def receive_article(article: ArticleInput):
    global latest_article_name
    # Store the article name in the global variable
    latest_article_name = article.name
    # Acknowledge receipt of the article name
    return {"message": "Article received", "article_name": article.name}

# Define a GET endpoint for the root path
@app.get("/")
def read_root():
    if latest_article_name:
        return {"message": f"Most recent article: {latest_article_name}"}
    else:
        return {"message": "No articles posted yet."}
### this shows the msg {"message":"Most recent article: minni"}
### when you do the try out post and execute 
