from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional, List

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name='Patryk', age=5),
    Person(id=2, name='Ola', age=10),
    Person(id=3, name='Paula', age=11)
]


@app.get('/api')
def read_root():
    return DB

@app.get('item/{item_id}')
def read_item(item_id:int, q:Optional[str]=None):
    return {'item_id': item_id, 'q': q}
