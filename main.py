from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel # Use to validate input
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]

# Request Get method url: "/""
@app.get("/")
async def root():
    return {"message": "Welcome my api !!!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts} 


@app.post("/createposts")
def create_posts(post: Post):
    # print(post)
    # print(post.dict())
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
   
    my_posts.append(post_dict)
    return {"data": post_dict}
    # return {"new_post": f"title {payload['title']} content: {payload['content']}"}

@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return {"post_detail": f"Here is post {id}"}
