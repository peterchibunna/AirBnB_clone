#!/usr/bin/python3
"""
This is the main interface for the HBNB console
"""
import cmd
import shlex
import re

from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


classes = {'BaseModel': BaseModel, 'User': User, 'City': City, 'Place': Place,
           'Review': Review, 'State': State, 'Amenity': Amenity}


class HBNBCommand(cmd.Cmd):
    """hbnb command prompt"""
    prompt = '(hbnb) '

    def default(self, arg):
        """Default behaviour of command interpreter"""
        methods = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in methods:
                    call = "{} {}".format(arg1[0], command[1])
                    return methods[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, arg):
        """Exits the program"""
        quit()
        return (1)

    def do_quit(self, arg):
        """Exits the program"""
        quit()
        return (1)

    def do_help(self, args):
        """Gives details about commands"""
        cmd.Cmd.do_help(self, args)

    def do_create(self, arg):
        """Creates new instance of BaseModel"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return (0)
        if args[0] in classes:
            inst = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return (0)
        print(inst.id)
        inst.save()

    def do_show(self, arg):
        """
        Prints string representation of an instance
        based on the class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return (0)
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("**class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = shlex.split(arg)
        myList = list()
        if len(args) == 0:
            for k in storage.all().values():
                myList.append(str(k))
            print("[", end="")
            print(", ".join(myList), end="")
            print("]")
        elif args[0] in classes:
            for key in storage.all():
                if args[0] in key:
                    myList.append(str(storage.all()[key]))
            print("[", end="")
            print(", ".join(myList), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    obj = storage.all()[key]
                    whitelist = ['created_at', 'updated_at', 'id']
                    if obj:
                        parser = shlex.split(arg)
                        if len(parser) < 3:
                            print("** attribute name missing **")
                        elif len(parser) < 4:
                            print("** attribute value missing **")
                        elif parser[2] not in whitelist:
                            obj.__dict__[parser[2]] = parser[3]
                            obj.__dict__['updated_at'] = datetime.now()
                            storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_count(self, clsName):
        """Retrieves number of instances of a class"""
        count = 0
        objs = storage.all()
        for k in objs.keys():
            myList = k.split('.')
            if myList[0] == clsName:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
