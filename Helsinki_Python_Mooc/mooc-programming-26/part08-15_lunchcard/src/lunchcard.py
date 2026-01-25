class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_lunch(self):
        lunch_cost = 2.6
        if self.balance >= lunch_cost:
            self.balance -= lunch_cost
    
    def eat_special(self):
        special_cost = 4.6
        if self.balance >= special_cost:
            self.balance -= special_cost

    def deposit_money(self, deposit: int):
        if deposit < 0:
            raise ValueError("ValueError: You cannot deposit an amount of money less than zero")
        self.balance += deposit

peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
peters_card.deposit_money(20)
graces_card.eat_special()
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")