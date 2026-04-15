from taskctl.core.json_storage import JSONStorage

def run(args):
    
    if not args:
        print('Usage: taskctl remove <task_id>')
        print("Example: taskctl remove 1")
        return
    
    try:
        id = int(args[0])
        storage = JSONStorage()
        status_message = storage.remove(id)
        print(status_message)
    except ValueError:
        print('Error: Task id must be integer value.')
        print('Usage: taskctl remove <task_id>')
        print("Example: taskctl remove 1")
        return
    except Exception as e:
        print(f'Error: {e}')
