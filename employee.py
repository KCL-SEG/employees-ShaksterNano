"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:

    def __init__(self, name, payment, *args):
        self.name = name
        self.payments = []
        self.payments.append(payment)
        for arg in args:
            self.payments.append(arg)

    def get_pay(self):
        total = 0
        for payment in self.payments:
            total += payment.get_pay()
        return total

    def __str__(self):
        string = f'{self.name} '
        for i in range(len(self.payments)):
            if i == len(self.payments) - 1:
                if len(self.payments) > 1:
                    string += "and "
                string += f"{self.payments[i]}.  Their total pay is {self.get_pay()}."
            else:
                string += f"{self.payments[i]}"
                if i < len(self.payments) - 2:
                    string += ","
                string += " "
        return string


class Payment:

    def get_pay(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class MonthlySalary(Payment):

    def __init__(self, salary):
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f"works on a monthly salary of {self.salary}"


class HourlyContract(Payment):

    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def get_pay(self):
        return self.hours * self.rate

    def __str__(self):
        return f"works on a contract of {self.hours} hours at {self.rate}/hour"


class BonusCommission(Payment):

    def __init__(self, bonus):
        self.bonus = bonus

    def get_pay(self):
        return self.bonus

    def __str__(self):
        return f"receives a bonus commission of {self.bonus}"


class ContractCommission(Payment):

    def __init__(self, contracts, rate):
        self.contracts = contracts
        self.rate = rate

    def get_pay(self):
        return self.contracts * self.rate

    def __str__(self):
        return f"receives a commission for {self.contracts} contract(s) at {self.rate}/contract"


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", MonthlySalary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", HourlyContract(100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", MonthlySalary(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", HourlyContract(150, 25), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", MonthlySalary(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", HourlyContract(120, 30), BonusCommission(600))
