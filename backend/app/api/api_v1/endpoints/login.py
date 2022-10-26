from datetime import timedelta

from typing import Any
from fastapi import (
    APIRouter, 
    Body, 
    Depends, 
    Form, 
    HTTPException,
    status
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.engine import Connection

# In app modules
from app.api.dependencies import (
    DBConnection,
    get_current_active_user
)
from app.core.config import settings
from app.core.security import (
    create_access_token,
    get_password_hash
)
from app.db.crud import (
    CRUDUser
)
from app.schemas import (
    UserOutDb,
    UserCreate,
    Token,
    UsersAll,
    Users
)

router = APIRouter()

@router.post('/login/authenticate', response_model=Token)
def get_user(
    db: Connection = Depends(DBConnection.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = CRUDUser.authenticate(
        connection=db,
        username=form_data.username,
        plain_password=form_data.password
    )
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )
    print(user.is_active)
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Inactive user',
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            'sub': user.username
        },
        expires_delta=access_token_expires
    )
    return Token(
        access_token=access_token,
        token_type='bearer'
    )

@router.post('/register')
async def register(
    username: str = Form(),
    password: str = Form(),
    db: Connection = Depends(DBConnection.get_db)
):
    user = CRUDUser.get_by_username(db, username=username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Username bisy',
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )
    try:
        user = UserCreate(
            username=username,
            password=get_password_hash(password=password),
            is_active=True
        )
        print(user)
        CRUDUser.insert_user(db, user.dict())
    except Exception as e:
        raise e
    return status.HTTP_201_CREATED
    
@router.get('/users/me', response_model=UserOutDb)
async def get_user_me(
    current_user: UserOutDb = Depends(get_current_active_user)
):
    return current_user

@router.get('/users/all', response_model=UsersAll)
async def get_all_users(
    current_user: UserOutDb = Depends(get_current_active_user),
    db: Connection = Depends(DBConnection.get_db)
):
    ans = CRUDUser.get_all(db)
    return ans

@router.get('/users/is_admin')
async def get_is_admin(
    current_user: UserOutDb = Depends(get_current_active_user),
    db: Connection = Depends(DBConnection.get_db)
):
    user = CRUDUser.is_admin(db, current_user.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='no user',
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )
    return user
