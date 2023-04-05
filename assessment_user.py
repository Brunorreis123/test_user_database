from settings import DatabaseType, UserAcessLevel, Database
from typing import Dict, List, Any, Union
from datetime import datetime
import uuid


class User:
    database: Database

    def __init__(self, database: Database, user_data: Dict[str, Union[str, UserAcessLevel]], role: str = '') -> None:
        self.acess_level = None
        self.database = database
        self.email = user_data['email']
        self.acess_level = user_data['acess_level']
        self.role = role
        self.registered_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.database.data['user'] = self.database.data.get('user', [])
        self.database.data['user'].append({
            'id': self.id,
            'email': self.email,
            'acess_level': self.acess_level,
            'role': self.role,
            'registered_at': self.registered_at
        })

    def save(self) -> None:
        user = {'id': self.id,
                'email': self.email,
                'acess_level': self.acess_level,
                'role': self.role,
                'registered_at': self.registered_at}
        self.database.data['user'].append(user)
