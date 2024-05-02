class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        operation = (f"added {num1} to {num2} got {result}")
        self.history.append(operation)
        return result
    def multiply(self, num1, num2):
        result = num1 * num2
        operation = (f"added {num1} to {num2} got {result}")
        self.history.append(operation)
        return result

    def print_operations(self):
        print("Operation history")
        for operation in self.history:
            print(operation)


calc = Calculator()
print(calc.add(3, 7))
print(calc.multiply(3, 7))
calc.print_operations()



