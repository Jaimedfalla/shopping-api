from typing import Optional
from fastapi import FastAPI, Body, Query, Path
from Models import Person

app = FastAPI()

@app.post("/person/new")
def create_person(person: Person = Body(...)):# The sign "..." indicates that a parameter is required in the request
    return person

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1,
        max_length=50,
        title= "Person name",
        description= "This is the person name. It's between 1 and 50 characters",
        example="Jaime"
        ), #name is optional parameter and its default value is None
    age: int=Query(
        ...
        ,ge=1,
        title= "Person age",
        description= "This is the person age. It's required",
        example= 38
        ) # ge -> greater or equal than. le -> less or equal than. gt -> greater than. lt -> less than
):
    return {name:age}

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt = 0,
        title= "Person Id",
        description= "This is person id. It's required and it must be greater than 0",
        example=2
        )
    ):
    return {person_id: "It exists"}

@app.put("/person/{person_id}")
def update_person(
    person_id:int = Path(
        ...,
        gt=0,
        title= "Person Id",
        description= "This is the person id. It's required and greater than 0",
        example=2
        ),
    person: Person = Body(...)
    ):

    return person