#!/usr/bin/python3
"""A module for our console interpreter"""

from models.basemodel import BaseModel
from models.user import User
from models.reviews import Review
from models import storage
import cmd


classes = {"BaseModel": BaseModel, "User": User, "Review": Review}

class Query_IP(cmd.Cmd):
    """A class that serves as an entry point into our
    console interpreter"""
    intro = 'Welcome professor!'
    prompt = '(query) '

    def do_quit(self, line):
        """quits the console interpreter"""
        return True
    
    def help_quit(self):
        print("Press CTRL-D or type quit to exit console interpreter")

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def help_EOF(self):
        print("Exit the program")

    def emptyline(self):
        """An empty line and enter should not do anything"""
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel"""
        if line:
            if line in classes:
                new_inst = eval(line + '()')
                print(new_inst.id)
                new_inst.save()
            else:
                print("**class dosen't exist**")
        else:
            print("**class name missing**")

    def help_create(self):
        print("create's a new instance of a class and prints it's id")

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        arg = args.split(' ')
        if arg[0]:
            if arg[0] in classes:
                if len(arg) == 2:
                    key = "{}.{}".format(arg[0], arg[1])
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("**no instance found!**")
                else:
                    print("**instance id missing**")
            else:
                print("**class dosen't exist**")
        else:
            print("**class name missing**")

    def help_show(self):
        print("Prints the string representation of an instance\
 based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.")
        
    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234."""
        arg = args.split(' ')
        if arg[0]:
            if arg[0] in classes:
                if len(arg) == 2:
                    key = "{}.{}".format(arg[0], arg[1])
                    if key in storage.all():
                        del storage.all()[key]
                        storage.save()
                        print("instance destroyed!")
                    else:
                        print("**no instance found!**")
                else:
                    print("**instance id missing**")
            else:
                print("**class dosen't exist**")
        else:
            print("**class name missing**")

    def help_destroy(self):
        print(" Deletes an instance based on the class name and id\ (save the change into the JSON file).\
 Ex: $ destroy BaseModel 1234-1234-1234.")
        
    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all."""
        new_list = []
        if arg:
            if arg in classes:
                for key in storage.all().keys():
                    cls_name = key.split('.')[0]
                    if cls_name == arg:
                        new_list.append(str(storage.all()[key]))
                        print(new_list)
            else:
                print("**class dosen't exist**")
        else:
            print("**class name missing**")

    def help_all(self):
        print("Prints all string representation of all instances\
 based or not on the class name. Ex: $ all BaseModel or $ all.")
        
    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""
    
        arg = args.split(' ')
    
        # Check if class name is provided
        if arg[0]:
            if arg[0] in classes:  # Check if the class exists in valid classes
                if arg[1] and len(arg) >= 3:  # Check if instance id is provided and enough arguments are given
                    key = "{}.{}".format(arg[0], arg[1])
                    if key in storage.all():  # Check if the instance key exists
                        if arg[2] and len(arg) >= 4:  # Check if attribute name is provided and enough arguments are given
                            if arg[3]:  # Check if value is provided
                                # Assuming self refers to an instance of the class
                                setattr(storage.all()[key], str(arg[2]), str(arg[3]))  # Update the attribute
                                storage.save()  # Save changes
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found! **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


                
        





if __name__ == '__main__':
    Query_IP().cmdloop()