from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.core.logger import logger
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = (db.query(User).filter(User.email == user.email).first())
    if existing:
        raise HTTPException(
            400,
            "Email already exists"
        )

    new_user = User(
        email=user.email,
        password=hash_password(
            user.password
        )
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info(
        f"User registered | email={new_user.email}"
    )
    return new_user


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = (
        db.query(User)
        .filter(
            User.email == form_data.username
        )
        .first()
    )

    if (
        not db_user
        or not verify_password(
            form_data.password,
            db_user.password
        )
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": db_user.email
        }
    )

    logger.info(
        f"Login successful | email={db_user.email}"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }