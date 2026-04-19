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
            print(f'id: {task["id"]}')
            print(f'{task["description"]}')
            print(f'status: {task["status"]}')
            print(f'created_at: {task["created_at"]}')
            print(f'updated_at: {task["updated_at"]}')
            print('-' * 40)
