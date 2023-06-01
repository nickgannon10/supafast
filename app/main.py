from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randint


from supabase import Client, create_client
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.on_event("startup")
def startup_event():
    data = supabase.table("posts").select("*").execute()
    print(data)

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None
#     id: Optional[int] = None

# my_posts = [{"title": "title1", "content": "content1", "published": True, "rating": 5, "id": 1}, 
#             {"title": "title2", "content": "content2", "published": True, "rating": 4 , "id": 2}]

# @app.get("/posts")
# async def themes():
#     response = supabase.table('posts').select('*').execute()
#     return response



# def user_exists(key: str = "id", value: str = None):
#     user = supabase.from_("users").select("*").eq(key, value).execute()
#     return len(user.data) > 0

# # Create a new user
# @app.post("/user")
# def create_user(user: Post):
#     try:
#         # Convert email to lowercase
#         user_id = user.id()

#         # Check if user already exists
#         if user_exists(value=user_id):
#             return {"message": "User already exists"}

#         # Add user to users table
#         user = supabase.from_("users")\
#             .insert({"title": user.name, "content": user.content, "published": user.published, "id": 1})\
#             .execute()

#         # Check if user was added
#         if user:
#             return {"message": "User created successfully"}
#         else:
#             return {"message": "User creation failed"}
#     except Exception as e:
#         print("Error: ", e)
#         return {"message": "User creation failed"}


# @app.get("/")
# async def root():

#     return {"message": "Hello World Nick"}

# def find_post(id: int):
#     for post in my_posts:
#         if post["id"] == id:
#             # type dict
#             return post

# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}

# @app.post("/posts")
# def create_post(post: Post, status_code=status.HTTP_201_CREATED):
#     post_dict = post.dict()
#     post_dict["id"] = randint(0, 100000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_post(id)
#     if not post: 
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
#     return {"data": post}

# @app.delete("/posts/{id}")
# def delete_post(id: int, status_code=status.HTTP_204_NO_CONTENT):
#     post = find_post(id)
#     if not post: 
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
#     my_posts.remove(post)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     post_found = find_post(id)
#     if not post_found: 
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
#     post_found["title"] = post.title
#     post_found["content"] = post.content
#     post_found["published"] = post.published
#     post_found["rating"] = post.rating
#     return {"data": post_found}

