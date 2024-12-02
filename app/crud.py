from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models
from app.core.db import get_db
from app.core.security import verify_password


def get_user_by_email(email, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user


def authenticate(
    user_credentials: OAuth2PasswordRequestForm, db: Session = Depends(get_db)
):
    db_user = get_user_by_email(user_credentials.username, db=db)
    if not db_user:
        return None
    if not verify_password(user_credentials.password, db_user.password):
        return None
    return db_user
