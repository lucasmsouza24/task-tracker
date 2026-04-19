from taskctl.core.json_storage import JSONStorage

def run(args):
    storage = JSONStorage()
    
    data_dict = storage.read()
    tasks = data_dict.get('tasks', [])
    
    if len(tasks) == 0:
        print('There is no signed tasks. Run add command to add tasks: \n> taskctl add "some task"')
    else:
        print('-' * 40)
        for task in tasks:
            print(f'id: {task.get("id", "N/A")}')
            print(f'{task.get("description", "N/A")}')
            print(f'status: {task.get("status", "N/A")}')
            print(f'created_at: {task.get("created_at", "N/A")}')
            print(f'updated_at: {task.get("updated_at", "N/A")}')
            print('-' * 40)
