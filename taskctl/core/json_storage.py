from pathlib import Path
import json

class JSONStorage:
    
    def __init__(self, file_name: str = 'data.json'):
        self.path = Path(file_name)
        self.template_path = 'taskctl/core/data.json.template'

    def exists(self) -> bool:
        return self.path.exists()

    def create(self) -> None:
        if not self.exists():
            initial_data = {
                "next_id": 1,
                "tasks": []
            }
            
            with open(self.path, 'w') as file:
                file.write(json.dumps(initial_data, indent=2))

    def read(self):
        if not self.exists():
            self.create()
        
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def add_task(self, task_string) -> None:
        data = self.read()
        data['tasks'].append(task_string)
        data['next_id'] += 1
        
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def get_next_id(self):
        data = self.read()
        return data['next_id']
