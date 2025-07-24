from datetime import date

def calculate_balance(principal, annual_rate, start_date, end_date):
    # Calculate the number of days between the start and end dates
    days = (end_date - start_date).days
    
    # Convert annual rate to daily rate
    daily_rate = annual_rate / 100 / 365
    
    # Apply daily compounding interest formula
    balance = principal * (1 + daily_rate) ** days
    return balance

# Input details
principal = 1000  # Initial deposit
annual_rate = 2.01  # Annual interest rate in percent
start_date = date(2024, 3, 16)  # Account opening date
end_date = date(2025, 7, 22)  # Today's date


# Calculate the balance
balance = calculate_balance(principal, annual_rate, start_date, end_date)

print(f"Your balance on {end_date} will be ${balance:.2f}")