"""
class Calculator:
    def addition(self, num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1 - num2
       
a = Calculator()       
result_1 = a.addition(2, 8)
result_2 = a.subtraction(8, 2)
print(result_1, result_2)

"""
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def addition(self):
        return self.num1 + self.num2
    def subtraction(self):
        return self.num1 - self.num2
    
a = Calculator(2, 8)
result_1 = a.addition()
result_2 = a.subtraction()
print(result_1, result_2)
