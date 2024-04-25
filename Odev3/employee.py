class Employee:
    def __init__(self, name: str, department: str, yearsOfWork: int, salary: float) -> None:
        self.name: str = name
        self.department: str = department
        self.yearsOfWork:int = yearsOfWork
        self.salary: float = salary

    def __str__(self) -> str:
        return f"{self.name}, {self.department}, {self.yearsOfWork}, {self.salary}"
