from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)



# redirect users to all page
@app.get("/")
def index():
    return RedirectResponse(url='/api/add')

# works too
@app.get("/api/all")
def index(db: Session = Depends(get_db)):
    return db.query(models.Person).all()

# Done
@app.post("/api/add" )
async def add(item: models.Item, db: Session = Depends(get_db)):
    person = models.Person()

    # error checking
    # if db.query(person).filter(models.Person.name == item.name).first():
    #      raise HTTPException(status_code=400, detail="Item already exists")
    
    person.name = item.name
    person.age = item.age
    person.track = item.track

    db.add(person)
    db.commit()

    return {
        "success":"True",
        "message":"Added successfully!"
    }

# Get person by name works
@app.get("/api/{name}")
def read(name:str, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.name == name).first()
    return person

# Done and works
@app.put("/api/update/{name}")
def update(name:str, item:models.Item,  db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.name == name).first()

    person.name = item.name
    person.age = item.age
    person.track = item.track

    db.add(person)
    db.commit()
    return {
        "success":"True",
        "message":"Updated successfully!"
    }

# Works
@app.delete("/api/delete/{name}")
def delete(name:str, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.name == name).first()

    db.delete(person)
    db.commit()

    return {
        "success":"True",
        "message":"Deleted successfully!"
    }
