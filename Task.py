class task :
    def __init__(self, task_name ):
        self.name = task_name
        self.description = None

    def set_description(self, task_description) :
         self.description = task_description

    def get_description(self):
         return self.description

    def set_name(self, task_name):
         self.name = task_name

    def get_name(self):
         return self.name

class task_math(task) :
    def __init__(self, task_name, task_description):  
        super().__init__(task_name, task_description) 

class task_item(task) :
    def __init__(self, task_name, task_description):  
        super().__init__(task_name, task_description) 
        self.required_item = None

    def completing_task(self, input_item) :

        if input_item == self.required_item: 

            print("You completed" + self.name) 

            return True 

        else: 
            print("This is no the right item for " + self.name) 

            return False   

 