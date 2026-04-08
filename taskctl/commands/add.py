from taskctl.core.task import Task
from taskctl.core.json_storage import JSONStorage

def run(args):
    
    if not args:
        print('Usage: taskctl add <task>')
        print("Example: taskctl add 'do homework'")
        return
    
    description = args[0]
    
    storage = JSONStorage()
    new_task = Task(description)
    storage.add_task(new_task.get_dict())
    