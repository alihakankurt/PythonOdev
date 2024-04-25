from typing import Callable
from employee import Employee

class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def list_employees(self) -> None:
        print(f"Employees in {self.name}: ")
        for (index, employee) in enumerate(self.employees):
            print(f"{index + 1} - {employee}")

    def raise_salary(self, predicate: Callable[[Employee], bool], raise_ratio: float) -> None:
        for employee in self.employees:
            if predicate(employee):
                employee.salary += employee.salary * (raise_ratio / 100)

    def remove_employee(self, employee: Employee) -> None:
        self.employees.remove(employee)
