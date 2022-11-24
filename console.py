#!/usr/bin/python3
"""
This is the main interface for the HBNB console
"""
import cmd
import shlex

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

    def EOF(self, arg):
        """Exits the program"""
        quit()
        return (1)

    def quit(self, arg):
        """Exits the program"""
        quit()
        return (1)

    def help(self, args):
        """Gives details about commands"""
        cmd.Cmd.help(self, args)

    def create(self, arg):
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

    def show(self, arg):
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

    def destroy(self, arg):
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

    def all(self, arg):
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
            print(", ".join(all_objects), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def update(self, arg):
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
                            obj.update_at = datetime.now()
                            storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
