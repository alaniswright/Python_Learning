from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


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

def find_posts(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


# Path operation / route
@app.get("/") # Decorator. Turns this function into a path operation. Using HTTP request method of GET. Value in brackets defines the path to perform the operation on. / is root path.
async def root(): # Function. Name doesn't matter. Use something descriptive
    return {"message": "Welcome to my API!!!"} 

@app.get("/posts")
def get_post():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
# Take what the API received from the post request, and ensure it matches the Post schema. 
# If it does, print it out and return it
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id):
    post = find_posts(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# put request to update
# quick check to see it exists
# if it does exist, take data from frontend and convert to dictionary
# replace post in my_posts with the one user has submitted
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}