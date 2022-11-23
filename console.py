#!/usr/bin/python3
"""
This is the main interface for the HBNB console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    intro = None
    prompt = '(hbnb) '
    """
    Command interpreter to manage the AirBnB objects.
    """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
