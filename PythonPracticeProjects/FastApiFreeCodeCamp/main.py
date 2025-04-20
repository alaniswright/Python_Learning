from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

# Pydantic schema 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True # Default value
    rating: Optional[int] = None # Optional field

# Array to store posts in memory
my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite foods", "content": "I like pizza", "id": 2}
]


# Path operation / route
@app.get("/") # Decorator. Turns this function into a path operation. Using HTTP request method of GET. Value in brackets defines the path to perform the operation on. / is root path.
async def root(): # Function. Name doesn't matter. Use something descriptive
    return {"message": "Welcome to my API!!!"} 

@app.get("/posts")
def get_post():
    return {"data": my_posts}

@app.post("/posts")
# Take what the API received from the post request, and ensure it matches the Post schema. 
# If it does, print it out and return it
def create_posts(post: Post):
    print(post.title)
    print(post.content)
    print(post.published)
    print(post.rating)
    print(post.dict())
    return {"data": post}

