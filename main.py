import base64
from datetime import datetime
import uuid
from fastapi import FastAPI, File, UploadFile
from connection import collection

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

    data = {"author":author, "title": title ,"data": str, "uploaded": datetime.now()}

    try:
        collection.insert_one(data)
    except:
        print('Error')

    return("Added successfully")


