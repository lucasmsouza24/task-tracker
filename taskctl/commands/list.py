from taskctl.core.json_storage import JSONStorage

def run(args):
    storage = JSONStorage()
    
    list_values = storage.read()
    
    print('-' * 40)
    for task in list_values:
        print(f'id: {task["id"]}')
        print(f'{task["description"]}')
        print(f'status: {task["status"]}')
        print(f'created_at: {task["created_at"]}')
        print(f'updated_at: {task["updated_at"]}')
        print('-' * 40)
