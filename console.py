#!/usr/bin/python3
"""
AirBnB Console

"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ cmd clone"""
    intro = 'Welcome to the Airbnb console. Type help or ? to list commands.\n'
    prompt = '(hobnob) '

    def __init__(self, completekey ='tab', stdin=None, stdout=None):
        """init method"""
        super().__init__(completekey, stdin, stdout)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit console"""
        return True

    def emptyline(self):
        """empty line. Do nothing"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
