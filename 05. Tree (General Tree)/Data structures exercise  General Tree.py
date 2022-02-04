# Created by Moontasir Abtahee at 2/4/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md

class GeneralTree:
    def __init__(self,name, designation):
        self.name = name
        self.designation =designation
        self.children = []
        self.parent = None

    def add_child(self,child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0

        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level
    def print_tree(self,cls):
        value = None
        cls = str(cls)
        if cls.isalpha():
            if cls == "name":
                value = self.name
            elif cls == "designation":
                value = self.designation
            elif cls == "both":
                value = f"{self.name}  ({self.designation})"

            space = " " * self.get_level() * 3
            prefix = space + '|___' if self.parent else " "
            print(prefix + value)
            if self.children:
                for i in self.children:
                    i.print_tree(cls)

        elif cls.isdigit():
            cls = int(cls)
            if cls<self.get_level():
                return

            value = f"{self.name}  ({self.designation})"
            space = " " * self.get_level() * 3
            prefix = space + '|___' if self.parent else " "
            print(prefix + value)
            if self.children:
                for i in self.children:
                    i.print_tree(cls)


def build_management_tree():
    root = GeneralTree("Nilupul","CEO")
    cto = GeneralTree("Chinmay","CTO")
    hr = GeneralTree("Gels","HR Head")

    root.add_child(cto)
    root.add_child(hr)

    infra = GeneralTree("Vishwa","Infrastructure Head")
    appli = GeneralTree("Aamir","Application Head")

    cto.add_child(infra)
    cto.add_child(appli)

    cloud = GeneralTree("Dhaval","Cloud Manager")
    app = GeneralTree("Abhijit","App Manager")

    infra.add_child(cloud)
    infra.add_child(app)

    recruit = GeneralTree("Peter","Recruitment Manager")
    policy = GeneralTree("Waqas","Policy Manager")

    hr.add_child(recruit)
    hr.add_child(policy)


    return root


root_node = build_management_tree()
root_node.print_tree("name")  # prints only name hierarchy
root_node.print_tree("designation")  # prints only designation hierarchy
root_node.print_tree("both")  # prints both (name and designation) hierarchy
print("+====================+")
root_node.print_tree(2)
root_node.print_tree(3)
