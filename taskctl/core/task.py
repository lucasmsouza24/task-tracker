from datetime import datetime
from enum import Enum

class Status(Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'

class Task:
    
    def __init__(self, id: int, description: str, status: Status = Status.TODO):
        self.id = id
        
        try:
            self.status = Status(status)
        except ValueError as e:
            self.status = Status.TODO
            
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status.value,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
        }

