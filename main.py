class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def work(self):
        print("Working...")

    def increase_salary(self, x):
        self._salary += x
        print(self._salary)


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self._team_size = team_size

    def manage(self):
        print("Managing...")


m1 = Manager("Ali", 1000, 5)

m1.work()
m1.manage()
m1.increase_salary(200)
