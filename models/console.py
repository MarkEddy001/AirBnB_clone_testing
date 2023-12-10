#!/usr/bin/python3
"""This module contains the class that is use for the console
    i.e, the entry point for the command intepreter
    """


import cmd
from models.base_model import BaseModel
from models import storage
import json
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import re


classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    """This class is a command intepreter"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """quit command to exit the program"""
        print()
        return True

    def emptyline(self):
        """do nothing when the line is empty"""
        pass

    def do_create(self, line):
        """create an instance of BaseModel"""
        if not line:
            print("** class name missing **")
        else:
            if line in classes:
                b1 = eval(line + "()")
                b1.save()
                print(b1.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """print the string implementation of an instance based
        on the class name and the id
        """
        all_objects = {}
        if not line:
            print("** class name missing **")
        else:
            command_list = line.split()
            class_name = command_list[0]
            if class_name in classes:
                if len(command_list) == 1:
                    print("** instance id missing **")
                else:
                    try:
                        with open("file.json", "r") as f:
                            if os.path.getsize("file.json") != 0:
                                all_objects = json.load(f)
                    except IOError:
                        pass
                    id_value = command_list[1]
                    obj = all_objects.get(class_name + "." + id_value, -1)
                    if obj == -1:
                        print("** no instance found **")
                    else:
                        instance = eval(class_name + "(**obj)")
                        print(instance)
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        all_objects = {}
        if not line:
            print("** class name missing **")
        else:
            command_list = line.split()
            class_name = command_list[0]
            if class_name in classes:
                if len(command_list) == 1:
                    print("** instance id missing **")
                else:
                    try:
                        with open("file.json", "r") as f:
                            if os.path.getsize("file.json") != 0:
                                all_objects = json.load(f)
                    except IOError:
                        pass
                    id_value = command_list[1]
                    obj = all_objects.get(class_name + "." + id_value, -1)
                    if obj == -1:
                        print("** no instance found **")
                    else:
                        del all_objects[class_name + "." + id_value]
                        with open("file.json", "w") as f:
                            json.dump(all_objects, f)
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances based or\
                not on the class name. Ex: $ all BaseModel or $ all"""
        all_objects = {}
        list_objects = []

        if line and line not in classes:
            print("** class doesn't exist **")
        else:
            try:
                with open("file.json", "r") as f:
                    if os.path.getsize("file.json") != 0:
                        all_objects = json.load(f)

                for obj in all_objects.keys():
                    class_name = all_objects[obj]["__class__"]
                    created_instance = eval(
                        class_name + "(**all_objects[obj])")
                    if line:
                        if line == class_name:
                            list_objects.append(str(created_instance))
                    else:
                        list_objects.append(str(created_instance))
            except IOError:
                pass
            finally:
                print(list_objects)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        Usage:
        update <class name> <id> <attribute> "<attribute value>"
        """
        all_objects = {}
        if not line:
            print("** class name missing **")
        else:
            command_list = line.split()
            class_name = command_list[0]
            if class_name in classes:
                if len(command_list) == 1:
                    print("** instance id missing **")
                else:
                    try:
                        with open("file.json", "r") as f:
                            if os.path.getsize("file.json") != 0:
                                all_objects = json.load(f)
                    except IOError:
                        pass
                    id_value = command_list[1]
                    obj = all_objects.get(class_name + "." + id_value, -1)
                    if obj == -1:
                        print("** no instance found **")
                    else:
                        if len(command_list) == 2:
                            print("** attribute name missing **")
                        elif len(command_list) == 3:
                            print("** value missing **")
                        else:
                            instance = eval(class_name + "(**obj)")
                            command_list[2] = command_list[2].strip("\"'")
                            setattr(instance, command_list[2],
                                    eval(command_list[3]))
                            instance.save()

            else:
                print("** class doesn't exist **")

    def default(self, line: str) -> None:
        """The default function that uses the do_<functions>
        to handle other commands:

        <class name>.all() -> retrieve all instances of a class
        <class name>.count() ->  retrieve the number of instances of a class
        <class name>.show(<id>) -> retrieve an instance based on its ID
        <class name>.destroy(<id> -> destroy an instance based on his ID
        <class name>.update(<id>, <attribute name>, <attribute value>) ->
                update an instance based on his ID
        <class name>.update(<id>, <dictionary representation>) ->
                update an instance based on his ID with a dictionary
        """
        error = cmd.Cmd.default
        list_cmds = ["all()", "count()"]
        args = line.split(".")
        obj_count = 0
        if (
            len(args) == 2
            and args[1] in list_cmds
            or args[1].startswith("show")
            or args[1].startswith("destroy")
            or args[1].startswith("update")
        ):
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                if args[0] not in classes:
                    print("** class doesn't exist **")
                    return
                all_objs = storage.all()
                for key in all_objs.keys():
                    if args[0] in key:
                        obj_count += 1
                print(obj_count)
            else:
                if "show" in args[1]:
                    check_show_command = re.search(
                        r'show\((["\'])([\s]?.*)\1\)', args[1]
                    )
                    # print(check_show_command)
                    if check_show_command:
                        id = check_show_command.group(2)
                        self.do_show(args[0] + " " + id)
                    else:
                        error(self, line)
                if "destroy" in args[1]:
                    check_destroy_command = re.search(
                        r'destroy\((["\'])([\s]?.*)\1\)', args[1]
                    )
                    if check_destroy_command:
                        id = check_destroy_command.group(2)
                        self.do_destroy(args[0] + " " + id)
                    else:
                        error(self, line)

                if "update" in args[1]:
                    check_update_command = re.search(
                        r'update\((["\'])([\s]?.*)\1\)', args[1]
                    )
                    check_update_command_dict = re.search(
                        r"update\(([\"'])(\s?.*?)\1,\s(\{.*\})\)", args[1]
                    )
                    if check_update_command:
                        li_update = check_update_command.group(2).split(", ")
                        update_command = ""
                        idx = 0
                        for x in li_update:
                            idx += 1
                            if idx == 3:
                                update_command += '"' + x.strip("\"'") + '"'
                            else:
                                update_command += x.strip("\"'") + " "
                        self.do_update(args[0] + " " + update_command)
                    elif check_update_command_dict:
                        id = check_update_command_dict.group(2)
                        try:
                            obj_dict = eval(check_update_command_dict.group(3))
                            if isinstance(obj_dict, dict):
                                for k, v in obj_dict.items():
                                    update_args = (
                                        args[0] + " " + id + " "
                                        + k + " " + repr(v)
                                    )
                                    self.do_update(update_args)
                            else:
                                error(self, line)
                        except SyntaxError:
                            error(self, line)

                    else:
                        error(self, line)
        else:
            cmd.Cmd.default(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
