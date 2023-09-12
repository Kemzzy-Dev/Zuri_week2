from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# To read a persons detail with the id of the person
@app.get("/api/{id}")
def index(id:int, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == id).first()
    if person == None:
        return HTTPException(status_code=404)
    return person

# To create a new person data in the database
@app.post("/api")
def add(item: models.Item, db: Session = Depends(get_db)):
    person = models.Person()

    person.name = item.name
    person.age = item.age
    person.track = item.track

    db.add(person)
    db.commit()

    return {
        "success":"True",
        "message":"Added successfully!"
    }

# Update a persons data in the database
@app.patch("/api/{id}")
async def add(id:str, item: models.Item, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == id).first()
    if person == None:
        return HTTPException(status_code=404)
    
    person.name = item.name
    person.age = item.age
    person.track = item.track

    db.add(person)
    db.commit()

    return {
        "success":"True",
        "message":"Updated successfully!"
    }

# Delete a persons data from the database
@app.delete("/api/{id}")
async def add(id:str, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == id).first()
    if person == None:
        return HTTPException(status_code=404)
    
    db.delete(person)
    db.commit()

    return {
        "success":"True",
        "message":"Deleted successfully!"
    }
