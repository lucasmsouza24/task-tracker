from datetime import datetime
from enum import Enum
from taskctl.core.json_storage import JSONStorage

class Status(Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'

class Task:
    
    def __init__(self, description: str, status: Status = Status.TODO):
        storage = JSONStorage()
        self.id = storage.get_next_id()
        
        try:
            self.status = Status(status)
        except ValueError as e:
            self.status = Status.TODO
            
        self.description = description
        now = datetime.now()
        self.created_at = now
        self.updated_at = now

    def get_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status.value,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
        }
