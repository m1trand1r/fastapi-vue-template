from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.engine import Connection


from app import schemas
from app.db.base import DBEngine, DBConnectionGetter
from app.db.crud import (
    CRUDUser
)
from app.core.config import settings
from app.core import security
from app.schemas.user import UserOutDb

engine = DBEngine().get_engine()
DBConnection = DBConnectionGetter(engine=engine)

oauth_scheme = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/login/authenticate'
)

def convert_to_dict(value) -> dict:
    return {key: value[key] for key in value.keys()}

async def get_current_user(
    db: Connection = Depends(DBConnection.get_db),
    token: str = Depends(oauth_scheme)
) -> UserOutDb:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Could not validate creditenals',
        )
    user = CRUDUser.get_by_username(db, token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    return UserOutDb(**convert_to_dict(user))

async def get_current_active_user(current_user: UserOutDb = Depends(get_current_user)) -> UserOutDb:
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Inactive user'
        )
    return current_user