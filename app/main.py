from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
import psycopg2
from pydantic import BaseModel # Use to validate input
from random import randrange
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='admin_fastapi', password='123456',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was successfully')
        break
    except Exception as error:
        print('Connection to Database failed')
        print('Error: ', error)
        time.sleep(2)


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# Request Get method url: "/""
@app.get("/")
async def root():
    return {"message": "Welcome my api !!!"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts} 


@app.post("/createposts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts(title, content, is_published) VALUES (%s, %s, %s) RETURNING * """, 
                    (post.title, post.content, post.published))
    
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}

@app.get("/posts/latest")
def get_latest_post():
    print(my_posts)
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/posts/{id}")
def get_post(id: str, response: Response):
    cursor.execute("""SELECT * FROM  posts WHERE id = %s""", (str(id)))
    post = cursor.fetchone()
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f'post with id: {id} was not found'}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={'message': f'post with id: {id} was not found'})
        
    # return {"post_detail": f"Here is post {id}"}
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    # find the index in the array that has require ID
    # my_posts.pop(index)
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    delete_post =  cursor.fetchone()
    conn.commit()

    if delete_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")

    return {"message": "post was successfully deleted"}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts set title = %s, content = %s, is_published = %s""", 
                   (post.title, post.content, post.published))

    updated_post = cursor.fetchone()

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id {id} does not exist")

    return {'data': updated_post}
