# Created by Moontasir Abtahee at 2/4/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elem =[]
        if self.left:
            elem += self.left.in_order_traversal()

        elem.append(self.data)

        if self.right:
            elem += self.right.in_order_traversal()

        return elem


    def Search(self,val):
        if val == self.data:
            return True

        if val > self.data:
            if self.right:
                return self.right.Search(val)
            else:
                return False

        elif val< self.data:
            if self.left:
                return self.left.Search(val)
            else:
                return False


    def find_min(self):
        if not self.left:
            return self.data

        else:
            return self.left.find_min()



    def find_max(self):
        if not self.right:
            return self.data
        else:
            return self.right.find_max()

    def calculate_sum(self):
        total = self.in_order_traversal()
        return sum(total)

    def post_order_traversal(self):
        elem = []
        if self.left:
            elem += self.left.post_order_traversal()
        if self.right:
            elem += self.right.post_order_traversal()

        elem.append(self.data)

        return elem
    def pre_order_traversal(self):
        elem = [self.data]
        if self.left:
            elem += self.left.pre_order_traversal()
        if self.right:
            elem += self.right.pre_order_traversal()

        return elem

    def Delete(self,val):
        if val>self.data:
            if self.right:
                self.right = self.right.Delete(val)
        elif val<self.data:
            if self.left:
                self.left = self.left.Delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.left
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.Delete(max_val)
        return self
def Build_BST(numbers):
    root_node = BinarySearchTreeNode(numbers[0])
    for i in range(1,len(numbers)):
        root_node.add_child(numbers[i])

    return root_node


bst = Build_BST([25,585,69,47,589,4,27,788,588,218,5148,648,426,5547,548,88,17,339,4,18,8,])
elem = bst.in_order_traversal()
print(elem)
print(bst.Search(5547))

print(bst.find_min())
print(bst.find_max())
print(bst.calculate_sum())
print("pre order Traversal")
print(bst.pre_order_traversal())
print("Post Order Traversal")
print(bst.post_order_traversal())

print("==============+==============+=============+============+======")
print()
print(bst.in_order_traversal())
bst.Delete(788)
print(bst.in_order_traversal())
print()