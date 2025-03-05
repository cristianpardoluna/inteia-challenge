import uuid
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from . import models, schemas
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def start_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/libros/", response_model=list[schemas.Book])
def list_books( author: Optional[str] = None, year: Optional[int] = None, db: Session = Depends(start_db)):
    """ Lista los libros, recibe parámetros de búsqueda `year` y `author`
    """
    query_params = []
    if author:
        query_params += (models.Book.author.ilike(f"%{author}%"))
    if year:
        query_params += (models.Book.author == year)

    return db.query(models.Book).filter(*query_params).all()

@app.get("/libros/{pk}", response_model=schemas.Book)
def retrieve_book(pk: str, db: Session = Depends(start_db)):
    """ Devuelve un libro basado en el parámetro PK,
        levanta HTTPException si no se encuentra
    """
    book = db.query(models.Book).filter(models.Book.id == pk).first()
    if book is None:
        raise HTTPException(status_code=404, detail="No se encontró el libro.")

    return book

@app.post("/libros/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(start_db)):
    """ Crea un libro
    """
    new_book = models.Book(**book.dict())
    new_book.id = str(uuid.uuid4())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.put("/libros/{pk}", response_model=schemas.Book)
def update_book(pk: str, book: schemas.BookCreate, db: Session = Depends(start_db)):
    """ Actualiza el libro relacionado al parámetro PK,
        levanta HTTPException si no se encuentra
    """
    db_book = db.query(models.Book).filter(models.Book.id == pk).first()
    if book is None:
        raise HTTPException(status_code=404, detail="No se encontró el libro.")
    for key, value in book.dict().items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/libros/{pk}")
def delete_book(pk: str, db: Session = Depends(start_db)):
    """ Elimina el libro basado en el parámetro PK de la URL,
        levanta HTTPException si no se encuentra
    """
    db_book = db.query(models.Book).filter(models.Book.id == pk).first()
    db.delete(db_book)
    db.commit()
    return Response(status_code=204)