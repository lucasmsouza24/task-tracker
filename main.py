#!/usr/bin/env python3

import sys

# commands
def add(args):
    print('ADD called with:', args)
    
def list_tasks(args):
    print('LIST called')

def remove(args):
    print('REMOVE called with args:', args)
    
COMMANDS = {
    'add': add,
    'list': list_tasks,
    'remove': remove,
}

# CLI entrypoint
def main():
    args = sys.argv[1:]
    
    if not args:
        print('Usage: task-cli <command> [args]')
        print('Commands:', ', '.join(COMMANDS.keys()))

    command = args[0]
    command_args = args[1:]
    
    func = COMMANDS.get(command)
    
    if not func:
        print('Unknow comand: {command}')
        print('Available commands: ', ', '.join(COMMANDS.keys()))
        return
    
    func(command_args)
    
if __name__ == "__main__":
    main()
