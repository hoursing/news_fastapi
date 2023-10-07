from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

# Request Get method url: "/""
@app.get("/")
async def root():
    return {"message": "Welcome my api !!!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"} 


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title {payload['title']} content: {payload['content']}"}
