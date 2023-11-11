from fastapi import FastAPI
from typing import Union
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#this extends BaseModel
class Post(BaseModel):
    title: str
    content: str
    #optional value
    published: bool = True
    #totally optional field
    rating: Optional[int] = None

#@app.get(...) - to specify urls for FastAPI
#async its basically sth about concurency, read about it later
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
#^specific url for different {item_id}
def read_item(item_id: int, q: Union[str, None] = None):
#^q can be either str or None, if q not provided it will be equal to None
    return {"item_id": item_id, "q":q}

#To run use unvicorn main:app --reload
#main is the name of the file without .py
#app is FastAPI() object
#--reload is used to relaod server after changes, WOW, moment after saving, WOW

@app.get("/posts")
def create_posts(new_post: Post):
    print(new_post.title)
    return {"hello"}

#title str, content str - 2 string essentially

#ORDER OF APIS CALLS IS IMPORTANT
#STATUS CODE REMEMBER, STATUS IN FASTAPI FOR EXAMPLE
#STATUS CODES!!!
#FAST API AUTOMATIC DOCUMMENTATION