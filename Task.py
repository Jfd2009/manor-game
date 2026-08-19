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
     
    def number(self, num1, num2, answer, input ):
        import random
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list2 = [1, 2, 3, 4]
        var1 = random.choice(list2)
        num1 = random.choice(list1)
        num2 = random.choice(list1)
        if var1 == 1 :
            print(num1, '+', num2, '=')
            print(num1 + num2)
        elif var1 == 2 :
            print(num1, '-', num2, '=')
            print(num1 - num2)
        elif var1 == 3 :
            print(num1, '/', num2, '=')
            print(num1 / num2)
        else:
            print(num1, 'x', num2, '=')
            print(num1 * num2)

class task_item(task) :
    def __init__(self, task_name, task_description):  
        super().__init__(task_name, task_description) 
        self.required_item = None

    def complete_task(self, input_item) :

        if input_item == self.required_item: 

            print("You completed" + self.name) 

            return True 

        else: 
            print("This is not the right item for " + self.name) 

            return False   

 