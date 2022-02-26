# Created by Moontasir Abtahee at 2/26/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
class Tree:
    def __init__(self,data , left= None ,right = None):
        self.data = data
        self.left = left
        self.right = right

    def TreeHeight(self,root):
        if root is None:
            return 0
        else:
            return 1+ max(self.TreeHeight(root.left),self.TreeHeight(root.right))

    def NodeLevel(self,root,data,level = 0):
        if root is None:
            return 0
        if root.data == data:
            return level

        levelID = self.NodeLevel(root.left,data,level+1)
        if levelID != 0:
            return levelID
        levelID = self.NodeLevel(root.right,data,level+1)
        if levelID != 0:
            return levelID

    def preOrder(self,root):
        print(root.data ,end="==>")
        if root.left:
            self.preOrder(root.left)
        if root.right:
            self.preOrder(root.right)

    def inOrder(self,root):
        if root.left:
            self.inOrder(root.left)
        print(root.data, end="==>")
        if root.right:
            self.inOrder(root.right)
    def postOrder(self,root):
        if root is None:
            return
        else:
            if self.left:
                self.postOrder(root.left)
            if self.right:
                self.postOrder(root.right)
            print(root.data ,end="==>")


    def copy(self,root,node = None,pointer = None):
        if node is None:
            node = root
        else:
            if pointer == "left":
                node.left = root
            elif pointer == "right":
                node.right = root

        if root:
            if root.left:
                self.copy(root.left,pointer= "left")
            if self.right:
                self.copy(root.right, pointer="right")
        else:
            return node



    def compare(self,tree1,tree2):
        if tree1 == None and tree2 == None:
            return True
        if tree1 and tree2 is not None:
            return tree1.data == tree2.data and self.compare(tree1.left,tree2.left) and self.compare(tree1.right,tree2.right)

        return False






root = Tree(1)
second_node = Tree(2)
thrd_node = Tree(3)
fourth_node = Tree(4)
fifth_node = Tree(5)
sixt_node = Tree(6)
seven_node = Tree(7)
eight_node = Tree(8)
root.left = second_node
root.right = thrd_node
thrd_node.left = fourth_node
thrd_node.right = fifth_node
fifth_node.left = sixt_node
fifth_node.right = seven_node
seven_node.left = eight_node

root.preOrder(root)
print()
root.postOrder(root)
print()
root.inOrder(root)
root.copy(root)
print()
root = Tree(1)
second_node = Tree(2)
thrd_node = Tree(3)
fourth_node = Tree(4)
fifth_node = Tree(5)
root.left = second_node
root.right = thrd_node
thrd_node.left = fourth_node
thrd_node.right = fifth_node
sixt_node = Tree(6)
seven_node = Tree(7)
eight_node = Tree(8)
fifth_node.left = sixt_node
fifth_node.right = seven_node
seven_node.left = eight_node


root2 = Tree(1)
second_node2 = Tree(2)
thrd_node2 = Tree(3)
fourth_node2 = Tree(4)
fifth_node2 = Tree(5)
root2.left = second_node2
root2.right = thrd_node2
thrd_node2.left = fourth_node2
thrd_node2.right = fifth_node2
sixt_node2 = Tree(6)
seven_node2 = Tree(7)
eight_node2 = Tree(8)
fifth_node2.left = sixt_node2
fifth_node2.right = seven_node2
seven_node2.left = eight_node2


if root.compare(root, root2) is True:
    print("Both two trees are exactly same")
else:
    print("two trees are not exactly same")