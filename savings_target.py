years = 30  
target_amount = 100000 
increment = 25  
rates = [0.01, 0.03, 0.05]  


def calculate_final_balance(monthly_saving, rate, years):
    annual_addition = monthly_saving * 12 
    balance = 0 
    for _ in range(years):
        balance = (balance + annual_addition) * (1 + rate) 
    return balance  

def find_required_monthly_saving(rate, years, target_amount, increment):
    monthly_saving = 100  
    while True:
        final_balance = calculate_final_balance(monthly_saving, rate, years)
        if final_balance >= target_amount:
            return monthly_saving
        monthly_saving += increment

for rate in rates:
    required_saving = find_required_monthly_saving(rate, years, target_amount, increment)
    print(f"To accumulate $100,000 in savings with an interest rate of {int(rate * 100)}%, you’ll need to save ${required_saving} each month.")





