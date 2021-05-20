def future_value_of_savings(initial_savings, years_saved, interest_rate):
    print(f"Your savings will be worth: ", initial_savings * (1 + (interest_rate / 100)) ** years_saved)

initial_savings = int(input("Initial savings: "))
years_saved = int(input("Years saved: "))
interest_rate = int(input("Interest rate: "))

future_value_of_savings(initial_savings, years_saved, interest_rate)
