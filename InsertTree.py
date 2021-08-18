class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def my_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Lenovo"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("Realme"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    my_tree()