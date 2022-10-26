from typing import Optional
from app.db.schema import users_table
from sqlalchemy.engine import Connection
from sqlalchemy import insert, Table 
from sqlalchemy.sql import select
# from app import schemas
from app.schemas import UserOutDb, Users, UsersAll, UserBase
from app.core.security import vertify_password
from app.db.base import convert_to_dict



class CRUDUser:
    @classmethod
    def get_by_username(cls, connection: Connection, username, table=users_table):
        value = connection.execute(
            select(
                table.c.username,
                table.c.password,
                table.c.is_active
            ).where(table.c.username == username)
        ).first()
        return value

    @classmethod
    def authenticate(cls, connection: Connection, username: str, plain_password: str) -> Optional[UserOutDb]:
        user = cls.get_by_username(connection=connection, username=username)
        if not user:
            return None
        user = convert_to_dict(user)
        user = UserOutDb(**user)
        if not vertify_password(plain_password, user.password):
            return None
        return user
        


    @classmethod
    def insert_user(cls, connection: Connection, ins_value: dict, table=users_table):
        try:
            connection.execute(
                insert(table),
                [
                    ins_value
                ]
            )
        except Exception as e:
            return e
        
    @classmethod
    def get_all(cls, connection: Connection, table=users_table):
        try:
            users = connection.execute(
                select(
                    table.c.id,
                    table.c.username,
                    table.c.password,
                    table.c.is_active,
                    table.c.is_superuser
                )
            ).all()
        except Exception as e:
            return e
        u_ret = []
        for user in users:
            u_ret.append(Users(**convert_to_dict(user)))
            
        u_ret = UsersAll(all_users=u_ret)
        
        return u_ret

    @classmethod
    def select_users(cls, connection: Connection, table=users_table) -> list:
        values = connection.execute(
            select(
                table.c.id,
                table.c.username,
                table.c.password
            )
        ).all()
        return values
    
    @classmethod
    def is_admin(cls, connection: Connection, username: str, table=users_table) -> bool | None:
        user = connection.execute(
            select(
                table.c.is_active,
                table.c.is_superuser
            ).where(table.c.username == username)
        ).first()
        if not user:
            return None
        user = UserBase(**convert_to_dict(user))
        return user.is_superuser
