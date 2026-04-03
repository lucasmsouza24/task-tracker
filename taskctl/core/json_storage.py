from pathlib import Path
import json
from taskctl.core.task import Task

class JSONStorage:
    
    def __init__(self, file_name: str = 'data.json'):
        self.path = Path(file_name)

    def exists(self) -> bool:
        return self.path.exists()

    def create(self) -> None:
        if not self.exists():
            with open(self.path, 'w') as file:
                file.write('[]')

    def read(self):
        if not self.exists():
            self.create()
        
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    
    def _write(self, string_values: str):
        with open(self.path, 'w') as file:
            file.write(string_values)

    def add_task(self, task: Task) -> None:
        dict_values = self.read()
        dict_values.append(task)
        self._write(json.dumps(dict_values))
