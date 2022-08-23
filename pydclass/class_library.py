#
# -*/*- PyDClass Library -*/*-
# Get class informations
# Author: VitriSnake
# License: GPLv3.0
#
# You can use this program but it's devlopped FOR PyDClass so please don't report if bug is detected into an other program using this library.
# Follow us on GitHub: https://github.com/CeltiumDev/PyDClass

# Imports
import inspect, importlib
import sys
import ipdb # /!\ For debug, you can safety delete this line.


class class_infos:
    def __init__(self, class_obj, module_obj, methods_list = [], attributes_list = []):
        self.class_obj = class_obj
        self.module_obj = module_obj
        self.methods_list = methods_list # For don't have parents/child
        self.attributes_list = attributes_list # For don't have parents/child

    def class_methods(self, name=False):
        class_members = inspect.getmembers(self.class_obj)
        class_methods = []
        for member in class_members:
            if inspect.isfunction(member[1]): # Check if is a method
                if not(member[1] in self.methods_list) and not(member[0].startswith('__')): 
                    if name == False:
                        self.methods_list.append(member[1])
                        class_methods.append(member[1])
                    elif name == True:
                        self.methods_list.append(member[1])
                        class_methods.append(member[0])
                    else:
                        raise ValueError('No valable values. -> name = True or False not '+str(name))

        return class_methods

    def class_atributes(self, methods_list):
        class_members = inspect.getmembers(self.class_obj())
        class_attributes_list = []
        for member in class_members:
            if not(member[0] in methods_list):
                if not(member[0].startswith('__')) and not(member[0] in self.methods_list):
                    class_attributes_list.append(member[0])
                    self.attributes_list.append(member[0])

        return class_attributes_list

    def class_parents(self):
        parents_list = []
        for p in self.class_obj.__bases__:
            if not(p.__name__.startswith('__')):
                if p.__name__ == "object":
                    pass
                else: 
                    parents_list.append(p)

        return parents_list

    def get_attributes_list(self):
        return self.attributes_list

    def get_methods_list(self):
        return self.methods_list

if __name__ == "__main__":
    import test1
    """
    1) Récupérer les class du module
    2) Faire passer le programme tout en fusionant les méthodes et attributs récupérés
    3) Retourner sous forme de dictionaire
    """
    members = inspect.getmembers(test1)
    class_list = []
    for m in members:
        if inspect.isclass(m[1]):
            class_list.append(m[1])

    attributes_h_list = []
    methods_h_list = []
    final_dict = []
    meth = []

    print(class_list)
    print(inspcet.getmembers)

    for c in class_list:
        ci = class_infos(c, test1, methods_h_list, attributes_h_list)
        meth_list = ci.class_methods()
        attr_list = ci.class_atributes(meth)
        parents_list = ci.class_parents()

        print(meth_list)
        print(attr_list)
        print(parents_list)

        dictionary = {"name": c.__name__, "methods": meth_list, "attributes": attr_list, "parents": parents_list}
        attributes_h_list += ci.get_attributes_list()
        methods_h_list += ci.get_methods_list()
        final_dict.append(dictionary)

    print(final_dict)
