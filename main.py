import base64
import collections
from datetime import datetime
import uuid, uvicorn
from fastapi import FastAPI, File, UploadFile
from connection import collection
from pydantic import BaseModel

# class Post(BaseModel):
#     id: str
#     artist: str
#     file: UploadFile = File(...)
#     created: datetime = datetime.now()

app = FastAPI()

@app.get("/")
async def index():
    return{"message: Hello there!"}

@app.post("/postImage")
async def image_post(author: str, title: str ,file: UploadFile = File(...)):
    #file = Post.file

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    str = base64.b64decode(contents)

    data = {"_id":author, "title": title ,"data": str, "uploaded": datetime.now()}
    
    collection.insert_one(data)

    return("added successfully")



if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)

