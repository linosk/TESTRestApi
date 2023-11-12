from fastapi import FastAPI
from typing import Union

app = FastAPI()

#@app.get(...) - to specify urls for FastAPI
#its basically sth about concurenccy, read about it later
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
#^specific url for different {item_id}s
def read_item(item_id: int, q: Union[str, None] = None):
#^q can be either str or None, if q not provided it will be equal to None
    return {"item_id": item_id, "q": q}

#Ro run use uvicorn main:app --reload
#main is the name of the file without .py
#app is FastAPI() object
#--reload is used to reload server after changes, WOW, moment after saving, WOW