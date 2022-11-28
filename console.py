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


def eval_args(args):
    check_for_dictionary = re.search(r"\{(.*?)\}", args)
    check_for_list = re.search(r"\[(.*?)\]", args)
    if check_for_dictionary is None:
        if check_for_list is None:
            return [i.strip(",") for i in shlex.split(args)]
        else:
            r = shlex.split(args[:check_for_list.span()[0]])
            return_list = [i.strip(",") for i in r]
            return_list.append(check_for_list.group())
            return return_list
    else:
        r = shlex.split(args[:check_for_dictionary.span()[0]])
        return_list = [i.strip(",") for i in r]
        return_list.append(check_for_dictionary.group())
        return return_list


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

        return cmd.Cmd.default(self, arg)

    def do_EOF(self, arg):
        """Exits the program"""
        # quit()
        return (1)

    def do_quit(self, arg):
        """Exits the program"""
        # quit()
        return (1)

    def emptyline(self):
        """empty line should not do anything"""
        pass

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
        """Prints string representation of an instance
        based on the class name and id"""
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
                key = args[0] + "." + args[1].replace(",", "")
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = shlex.split(arg)
        my_list = list()
        if len(args) == 0:
            for k in storage.all().values():
                my_list.append(str(k))
            print("[", end="")
            print(", ".join(my_list), end="")
            print("]")
        elif args[0] in classes:
            for key in storage.all():
                if args[0] in key:
                    my_list.append(str(storage.all()[key]))
            print("[", end="")
            print(", ".join(my_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""
        args2 = eval_args(arg)
        objects = storage.all()
        # print(args2)
        if len(args2) == 0:
            print("** class name missing **")
            return False
        if args2[0] not in classes:
            print("** class doesn't exist **")
            return False
        if args2.__len__() == 1:
            print("** instance id missing **")
            return False
        if "{class_name}.{id}".format(class_name=args2[0], id=args2[1]) \
                not in objects.keys():
            print("** no instance found **")
            return False
        if len(args2) == 2:
            print("** attribute name missing **")
            return False
        if len(args2) == 3:
            try:
                type(eval(args2[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args2) == 4:
            obj = objects["{class_name}.{id}".format(
                class_name=args2[0], id=args2[1])]
            # convert the data type of the value correctly
            try:
                obj.__dict__[args2[2]] = eval(args2[3])
            except NameError as e:
                obj.__dict__[args2[2]] = args2[3]
            obj.__dict__['updated_at'] = datetime.now()
            storage.save()

        elif type(eval(args2[2])) == dict:
            whitelist = ['created_at', 'updated_at', 'id']
            obj = objects["{class_name}.{id}".format(
                class_name=args2[0], id=args2[1])]
            for k, v in eval(args2[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}
                        and k not in whitelist):
                    try:
                        obj.__dict__[k] = eval(v.__str__())
                    except (NameError, TypeError):
                        obj.__dict__[k] = v.__str__()
                    # convert the data type correctly
                else:
                    # convert the data type correctly
                    try:
                        obj.__dict__[k] = eval(v)
                    except (NameError, TypeError) as e:
                        obj.__dict__[k] = v
            obj.__dict__['updated_at'] = datetime.now()
            storage.save()

    def do_count(self, args):
        """Retrieves number of instances of a class"""
        count = 0
        arguments_list = eval_args(args)
        objs = storage.all()
        for k in objs.keys():
            my_list = k.split('.')
            if my_list[0] == arguments_list[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
