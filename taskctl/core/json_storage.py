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

    def remove(self, id) -> None:
        data = self.read()
        tasks = data['tasks']
        
        new_tasks = [task for task in tasks if task['id'] != id]
        
        if len(new_tasks) == len(tasks):
            return f'Task {id} not found'   
        
        data['tasks'] = new_tasks
        
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
            return f'Success on delete task {id}'

    def read(self):
        if not self.exists():
            self.create()
        
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def add_task(self, task_string) -> None:
        data = self.read()
        tasks = data.get('tasks', [])
        next_id = self.get_next_id() + 1
        # data['tasks'].append(task_string)
        # data['next_id'] += 1
        tasks.append(task_string)
        
        data['next_id'] = next_id
        data['tasks'] = tasks
        
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def get_next_id(self):
        data = self.read()
        return data.get('next_id', 1)
