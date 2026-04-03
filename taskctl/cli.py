#!/usr/bin/env python3

from taskctl.commands import add, list, remove, mark
import sys

COMMANDS = {
    'add': add.run,
    'list': list.run,
    'remove': remove.run,
    'mark': mark.run,
}

# CLI entrypoint
def main():
    args = sys.argv[1:]
    
    if not args:
        print('Usage: taskctl <command> [args]')
        print('Commands:', ', '.join(COMMANDS.keys()))
        return

    command = args[0]
    command_args = args[1:]
    
    func = COMMANDS.get(command)
    
    if not func:
        print(f'Unknow comand: {command}')
        print('Available commands: ', ', '.join(COMMANDS.keys()))
        return
    
    func(command_args)

if __name__ == "__main__":
    main()