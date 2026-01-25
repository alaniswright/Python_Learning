# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance - amount >= 0:
            self.balance -= amount
            return True
        else:
             return False
        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        lunch_price = 2.5
        if payment - lunch_price >= 0:
            self.funds += lunch_price
            self.lunches += 1
            return payment - lunch_price
        else:
            return payment


    def eat_special(self, payment: float):
        special = 4.3
        if payment - special >= 0:
            self.funds += special
            self.specials += 1
            return payment - special
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        lunch = 2.5
        if card.balance >= lunch:
            card.balance -= lunch
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        special = 4.3
        if card.balance >= special:
            card.balance -= special
            self.specials += 1
            return True
        else:
            return False


    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)

if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)