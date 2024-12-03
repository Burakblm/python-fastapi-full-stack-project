from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api.deps import get_current_user
from app.core.db import get_db
from app.core.security import get_password_hash

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print(user)
    user_temp = crud.get_user_by_email(user.email, db=db)
    if user_temp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="this email is already in use",
        )

    hashed_password = get_password_hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/")
def get_user_data(
    db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
):
    user_data = db.query(models.User).filter(models.User.id == current_user.id).first()

    return user_data
