from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.engine import Connection

class DBEngine:
    def __init__(self) -> None:
        self.ENGINE_STRING = settings.DATABASE_URL

    def get_engine(self):
        return create_engine(self.ENGINE_STRING)

class DBConnectManager:
    def __init__(self, engine) -> None:
        self.engine = engine

    def __enter__(self) -> Connection:
        self.connection = self.engine.connect()
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.connection.close()

class DBConnectionGetter:
    def __init__(self, engine) -> None:
        self.engine = engine
    
    def get_db(self):
        self.engine
        with DBConnectManager(engine=self.engine) as connection:
            yield connection

def convert_to_dict(value):
    return {key: value[key] for key in value.keys()}

