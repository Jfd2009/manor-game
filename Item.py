class item :
    def __init__(self, item_name):
        self.name = item_name
        self.description = None 

    def describe(self):
        print(self.description) 

    def set_description(self, item_description):
        self.description = item_description
    
    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def describe(self): 
        print("The [" + self.name + "] is here - " + self.description) 