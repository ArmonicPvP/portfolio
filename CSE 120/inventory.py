class Inventory:
    def __init__(self, name, contents, carry_cap=99, droppable=True):
        self.carry_cap = carry_cap
        self.name = name
        self.droppable = droppable
        self.contents = contents
        self.contents = {}
        self.weight = 1

    def __str__(self):
        #makes it so when the class is called in a print statement, it returns the contents of the memory location rather
        #than just the memory location
        bag_contains = "Your {} contains:\n".format(self.name)
        for i in self.contents.keys():
            bag_contains += "{}\n".format(i)
        return bag_contains

    # search(item_Name)
    # returns an item but doesn't remove it from bag
#     def search(self, item_name):
#        item = self.contents.get(item_name)
#        if item:
#            bag_contains = "The {} contains:\n{}".format(self.name,item_name)
#        else:
#            bag_contains = "The {} does not contain {}.".format(self.name,item_name)
#         if item_name != None:
#             return self.contents[item_name]
#         else:
#             return self.contents

    def add(self, i_name, i_weight):
        #the add function allows items to be added to the inventory as well as with a weight for a capacity mechanic
        self.contents[i_name] = [i_name, i_weight]
        return

    # remove(item_Name)
    # returns an item and removes it from bag
    def remove(self, item_name):
        item = self.contents.get(item_name)
        if item:
            del self.contents[item_name]
            return item
        else:
            return None
        return
