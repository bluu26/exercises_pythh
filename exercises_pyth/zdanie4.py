class Employe:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = 0

    def set_salary(self, salary):
        if not isinstance(salary, (int, float)) or salary < 0:
            print("Salary must be a non-negative number.")
        else:
            self._salary = salary
            print("Salary set successfully.")

    def describe(self):
        print(f"Name: {self.first_name} {self.last_name}")


   TUTAJ MAMY CIEKAWY MOTYW Z SELF ID
class Employee:
    next_id = 1

    def __init__(self, imie, nazwisko):
        self.id = self.next_id
        Employee.next_id += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self._salary = None


    def set_salary(self, salary):
        if type(salary) in (int,float) and salary > 0:
            self._salary = salary
print(Employee.next_id)
e = Employee("Sławek", "Bogusławski")
print(Employee.next_id)
e2 = Employee( "Gosia", "Pe")
print(Employee.next_id)
print(e.id)
print(e2.id)