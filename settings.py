import enum
from enum import Enum
from typing import Dict, List, Any


class DatabaseType(Enum):
    memory = 'memory'
    mongodb = 'mongodb'


class UserAcessLevel(enum.Enum):
    normal = 1
    admin = 2


class Database:
    __instance = None

    def __init__(self, database_type: DatabaseType, data: Dict[str, List[Dict[str, Any]]] = {}) -> None:
        if data is None:
            data = {}
        if not database_type:
            raise ValueError
        if database_type == DatabaseType.mongodb:
            raise ValueError("The selected database type is not implemented yet")
        else:
            self.database_type = database_type
            self.data = data
            Database.__instance = self

    def get_instance(cls) -> 'Database':
        if not cls.__instance:
            cls.__instance = Database(DatabaseType.memory)
        return cls.__instance

