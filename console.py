#!/usr/bin/python3
""" import modules """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """ Body of HBNBCommand """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, arg):
        """ exit console """
        return True

    def do_EOF(self, arg):
        """ method of EOF """
        print()
        return True

    def emptyline(self):
        """ no line entered """
        pass

    def default(self, line):
         """default method"""
        lst = (line.replace('(', '.').replace(',', '.').replace(' ', '')
               [:-1].split('.'))
        if len(lst) > 1:
            if lst[1] == "all":
                return self.do_all(lst[0])

            elif lst[1] == "show":
                return self.do_show(lst[0] + ' ' + lst[2])

            elif lst[1] == "destroy":
                return self.do_destroy(lst[0] + ' ' + lst[2])

            elif lst[1] == "update":
                return (self.do_update(lst[0] + ' ' + lst[2] +
                                       ' ' + lst[3] + ' ' + lst[4]))

            elif lst[1] == "count":
                print(len(storage.all()))

        else:
            print("*** Unknown syntax: {}".format(line))
            return False

    def do_create(self, arg):
        """ create new instance """
        args = args.split()
        if not args:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        else:
            b = HBNBCommand.classes[args[0]]()
            b.save()
            print(b.id)

    def do_show(self, arg):
        """print instance"""
        arg = args.split()
        _all = storage.all()
        if not arg:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        else:
            print(_all["{}.{}".format(args.split()[0], args.split()[1])])

    def do_destroy(self, arg):
        """ Method to delete instance with class and id """
        arg = args.split()
        _all = storage.all()
        if not arg:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        else:
            del _all["{}.{}".format(args.split()[0], args.split()[1])]
            storage.save()

    def do_all(self, arg):
        """ print all instances """
        args = args.split()
        lst = []
        if args and args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif not args:
            for i in storage.all().values():
                lst.append(str(i))
        else:
            for i in storage.all().values():
                if args[0] == i.__class__.__name__:
                    lst.append(str(i))
        if len(lst):
            print(lst)

    def do_update(self, arg):
        """ update JSON file"""
         _all = storage.all()
        if len(args.split()) == 0:
            print("** class name missing **")

        elif args.split()[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        elif len(args.split()) == 2:
            print("** attribute name missing **")

        elif len(args.split()) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args.split()[0], args.split()[1])
            setattr(_all[key], args.split()[2],
                    re.search(r'\w+', args.split()[3]).group())
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
