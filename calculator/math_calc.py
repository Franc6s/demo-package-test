class calculator :

    def __init__(self):
        pass

    def add (self,a,b):
        return a + b
    
    def subtract (self,a,b):
        return a - b
    
    def divide(self,a,b):
        try: 
            return round((a/b),)
        except ZeroDivisionError:
            return "Error:Division by 0 is not allowed"

    def multiply(self,a,b):
        return a * b
    
calc = calculator()

 
 